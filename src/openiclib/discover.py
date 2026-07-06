from __future__ import annotations

import base64
import logging
from dataclasses import dataclass
from datetime import datetime

import httpx

from openiclib.types import CandidateRepo

logger = logging.getLogger(__name__)

TOPIC_QUERIES = [
    "skywater-pdk",
    "sky130",
    "ihp-sg13g2",
    "gf180mcu",
    "open-pdk",
    "asic-design",
    "open-source-silicon",
]

KEYWORD_QUERIES = [
    '"tapeout" pdk',
    '"silicon proven" pdk',
    '"open pdk" amplifier OR oscillator OR ADC',
    '"tape-out" ASIC',
    "pdk LNA OR TIA OR PGA OR VCO OR PLL",
]

KNOWN_ORGS = [
    "IHP-GmbH",
    "efabless",
    "google",
    "chipsalliance",
    "TinyTapeout",
]

API_BASE = "https://api.github.com"
RESULTS_PER_PAGE = 30
MAX_PAGES_PER_QUERY = 3


@dataclass
class TapeoutSource:
    org: str
    repo: str
    subpath: str = ""
    pdk_topic: str = ""
    skip_dirs: tuple[str, ...] = ("drc", "docs", "symbol", ".github", ".media", "fig", "workflows")
    info_file: str = "README.md"
    extra_topics: tuple[str, ...] = ()


IHP_TAPEOUT_REPOS: list[TapeoutSource] = [
    TapeoutSource("IHP-GmbH", "TO_Dec2023", pdk_topic="sg13g2"),
    TapeoutSource("IHP-GmbH", "TO_May2024", pdk_topic="sg13g2"),
    TapeoutSource("IHP-GmbH", "TO_Nov2024", pdk_topic="sg13g2"),
    TapeoutSource("IHP-GmbH", "TO_Dec2024", pdk_topic="sg13g2"),
    TapeoutSource("IHP-GmbH", "TO_Apr2025", pdk_topic="sg13g2"),
    TapeoutSource("IHP-GmbH", "TO_May2025", pdk_topic="sg13g2"),
    TapeoutSource("IHP-GmbH", "TO_July2025", pdk_topic="sg13g2"),
    TapeoutSource("IHP-GmbH", "TO_Sep2025", pdk_topic="sg13g2"),
    TapeoutSource(
        "IHP-GmbH",
        "IHP-Open-FMD_QNC-Tapeouts",
        pdk_topic="sg13g2",
        skip_dirs=("docs", ".github"),
    ),
    TapeoutSource(
        "IHP-GmbH",
        "Open-Silicon-MPW",
        pdk_topic="sg13g2",
        skip_dirs=("TRL-templates", "fig", "workflows", ".github"),
    ),
]

TT_TAPEOUT_REPOS: list[TapeoutSource] = [
    TapeoutSource(
        "TinyTapeout", "tinytapeout-06",
        subpath="projects", pdk_topic="sky130",
        info_file="info.yaml", extra_topics=("tinytapeout",),
    ),
    TapeoutSource(
        "TinyTapeout", "tinytapeout-07",
        subpath="projects", pdk_topic="sky130",
        info_file="info.yaml", extra_topics=("tinytapeout",),
    ),
    TapeoutSource(
        "TinyTapeout", "tinytapeout-08",
        subpath="projects", pdk_topic="sky130",
        info_file="info.yaml", extra_topics=("tinytapeout",),
    ),
    TapeoutSource(
        "TinyTapeout", "tinytapeout-10",
        subpath="projects", pdk_topic="sky130",
        info_file="info.yaml", extra_topics=("tinytapeout",),
    ),
    TapeoutSource(
        "TinyTapeout", "tinytapeout-ihp-0p1",
        subpath="projects", pdk_topic="sg13g2",
        info_file="info.yaml", extra_topics=("tinytapeout",),
    ),
    TapeoutSource(
        "TinyTapeout", "tinytapeout-ihp-0p2",
        subpath="projects", pdk_topic="sg13g2",
        info_file="info.yaml", extra_topics=("tinytapeout",),
    ),
    TapeoutSource(
        "TinyTapeout", "tinytapeout-ihp-26a",
        subpath="projects", pdk_topic="sg13g2",
        info_file="info.yaml", extra_topics=("tinytapeout",),
    ),
    TapeoutSource(
        "TinyTapeout", "tinytapeout-sky-25b",
        subpath="projects", pdk_topic="sky130",
        info_file="info.yaml", extra_topics=("tinytapeout",),
    ),
    TapeoutSource(
        "TinyTapeout", "tinytapeout-sky-26a",
        subpath="projects", pdk_topic="sky130",
        info_file="info.yaml", extra_topics=("tinytapeout",),
    ),
    TapeoutSource(
        "TinyTapeout", "tinytapeout-sky-26b",
        subpath="projects", pdk_topic="sky130",
        info_file="info.yaml", extra_topics=("tinytapeout",),
    ),
    TapeoutSource(
        "TinyTapeout", "tinytapeout-gf-0p2",
        subpath="projects", pdk_topic="gf180mcu",
        info_file="info.yaml", extra_topics=("tinytapeout",),
    ),
    TapeoutSource(
        "TinyTapeout", "tinytapeout-gf-0p3",
        subpath="projects", pdk_topic="gf180mcu",
        info_file="info.yaml", extra_topics=("tinytapeout",),
    ),
]

TAPEOUT_SOURCES: list[TapeoutSource] = IHP_TAPEOUT_REPOS + TT_TAPEOUT_REPOS


class GitHubDiscoverer:
    def __init__(self, token: str | None = None) -> None:
        headers: dict[str, str] = {"Accept": "application/vnd.github+json"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        self._client = httpx.AsyncClient(
            base_url=API_BASE,
            headers=headers,
            timeout=30.0,
        )
        self._seen: set[str] = set()

    async def __aenter__(self) -> GitHubDiscoverer:
        return self

    async def __aexit__(self, *exc) -> None:
        await self._client.aclose()

    async def _search_repos(self, query: str) -> list[dict]:
        results: list[dict] = []
        for page in range(1, MAX_PAGES_PER_QUERY + 1):
            resp = await self._client.get(
                "/search/repositories",
                params={"q": query, "per_page": RESULTS_PER_PAGE, "page": page},
            )
            if resp.status_code == 403:
                logger.warning("Rate limited on query %r, stopping pagination", query)
                break
            resp.raise_for_status()
            data = resp.json()
            items = data.get("items", [])
            results.extend(items)
            if len(items) < RESULTS_PER_PAGE:
                break
        return results

    async def _fetch_readme(self, owner: str, repo: str) -> str:
        try:
            resp = await self._client.get(f"/repos/{owner}/{repo}/readme")
        except Exception:
            logger.warning("Network error fetching README for %s/%s", owner, repo)
            return ""
        if resp.status_code != 200:
            return ""
        data = resp.json()
        content = data.get("content", "")
        encoding = data.get("encoding", "")
        if encoding == "base64" and content:
            try:
                return base64.b64decode(content).decode("utf-8", errors="replace")
            except Exception:
                return ""
        return content

    async def _fetch_file_content(self, owner: str, repo: str, path: str) -> str:
        try:
            resp = await self._client.get(f"/repos/{owner}/{repo}/contents/{path}")
        except Exception:
            logger.debug("Network error fetching %s/%s/%s", owner, repo, path)
            return ""
        if resp.status_code != 200:
            return ""
        data = resp.json()
        if not isinstance(data, dict):
            return ""
        content = data.get("content", "")
        encoding = data.get("encoding", "")
        if encoding == "base64" and content:
            try:
                return base64.b64decode(content).decode("utf-8", errors="replace")
            except Exception:
                return ""
        return content

    @staticmethod
    def _parse_info_yaml(raw: str) -> tuple[str, str]:
        """Extract title and description from a TinyTapeout info.yaml."""
        try:
            import yaml

            data = yaml.safe_load(raw)
            if not isinstance(data, dict):
                return "", ""
            project = data.get("project", {})
            title = project.get("title", "")
            desc = project.get("description", "")
            return str(title), str(desc)
        except Exception:
            return "", ""

    def _repo_to_candidate(self, item: dict, readme: str = "") -> CandidateRepo:
        updated = item.get("updated_at")
        return CandidateRepo(
            url=item.get("html_url", ""),
            owner=item.get("owner", {}).get("login", ""),
            name=item.get("name", ""),
            description=item.get("description") or "",
            readme_text=readme,
            topics=item.get("topics", []),
            stars=item.get("stargazers_count", 0),
            last_updated=datetime.fromisoformat(updated) if updated else None,
            source="github",
        )

    async def search_by_topics(self) -> list[CandidateRepo]:
        candidates: list[CandidateRepo] = []
        for topic in TOPIC_QUERIES:
            query = f"topic:{topic}"
            logger.info("Searching GitHub: %s", query)
            items = await self._search_repos(query)
            for item in items:
                url = item.get("html_url", "")
                if url in self._seen:
                    continue
                self._seen.add(url)
                candidates.append(self._repo_to_candidate(item))
        return candidates

    async def search_by_keywords(self) -> list[CandidateRepo]:
        candidates: list[CandidateRepo] = []
        for kw in KEYWORD_QUERIES:
            logger.info("Searching GitHub: %s", kw)
            items = await self._search_repos(kw)
            for item in items:
                url = item.get("html_url", "")
                if url in self._seen:
                    continue
                self._seen.add(url)
                candidates.append(self._repo_to_candidate(item))
        return candidates

    async def crawl_orgs(self) -> list[CandidateRepo]:
        candidates: list[CandidateRepo] = []
        for org in KNOWN_ORGS:
            logger.info("Crawling org: %s", org)
            resp = await self._client.get(
                f"/orgs/{org}/repos",
                params={"per_page": 100, "type": "public"},
            )
            if resp.status_code != 200:
                logger.warning("Failed to list repos for org %s: %d", org, resp.status_code)
                continue
            for item in resp.json():
                url = item.get("html_url", "")
                if url in self._seen:
                    continue
                self._seen.add(url)
                candidates.append(self._repo_to_candidate(item))
        return candidates

    async def add_known_repos(self, urls: list[str]) -> list[CandidateRepo]:
        candidates: list[CandidateRepo] = []
        for url in urls:
            if url in self._seen:
                continue
            self._seen.add(url)
            parts = url.rstrip("/").split("/")
            if len(parts) < 2:
                continue
            owner, name = parts[-2], parts[-1]
            resp = await self._client.get(f"/repos/{owner}/{name}")
            if resp.status_code != 200:
                logger.warning("Failed to fetch repo %s/%s: %d", owner, name, resp.status_code)
                continue
            item = resp.json()
            candidates.append(self._repo_to_candidate(item))
        return candidates

    async def crawl_tapeout_repos(
        self, sources: list[TapeoutSource] | None = None
    ) -> list[CandidateRepo]:
        if sources is None:
            sources = TAPEOUT_SOURCES
        candidates: list[CandidateRepo] = []
        for src in sources:
            path = src.subpath or ""
            api_path = f"/repos/{src.org}/{src.repo}/contents/{path}".rstrip("/")
            logger.info("Crawling tapeout repo: %s/%s/%s", src.org, src.repo, path)
            try:
                resp = await self._client.get(api_path)
            except Exception:
                logger.warning("Network error listing %s/%s/%s", src.org, src.repo, path)
                continue
            if resp.status_code != 200:
                logger.warning(
                    "Failed to list %s/%s/%s: %d", src.org, src.repo, path, resp.status_code
                )
                continue
            items = resp.json()
            if not isinstance(items, list):
                continue
            dirs = [
                i["name"]
                for i in items
                if i["type"] == "dir"
                and i["name"] not in src.skip_dirs
                and not i["name"].startswith(".")
            ]
            for dirname in dirs:
                sub = f"{path}/{dirname}" if path else dirname
                url = f"https://github.com/{src.org}/{src.repo}/tree/main/{sub}"
                if url in self._seen:
                    continue
                self._seen.add(url)

                topics = list(src.extra_topics)
                if src.pdk_topic:
                    topics.append(src.pdk_topic)
                topics.append("tapeout")
                topics.append("silicon-proven")

                description = ""
                readme_text = ""
                info_path = f"{sub}/{src.info_file}"

                raw = await self._fetch_file_content(src.org, src.repo, info_path)
                if raw and src.info_file.endswith(".yaml"):
                    title, desc = self._parse_info_yaml(raw)
                    description = f"{title} — {desc}" if title and desc else title or desc
                elif raw:
                    readme_text = raw

                candidates.append(
                    CandidateRepo(
                        url=url,
                        owner=src.org,
                        name=dirname,
                        description=description,
                        readme_text=readme_text,
                        topics=topics,
                        stars=0,
                        last_updated=None,
                        source="github-tapeout",
                    )
                )
            logger.info(
                "Found %d designs in %s/%s",
                len(dirs),
                src.org,
                src.repo,
            )
        return candidates

    async def fetch_readmes(self, candidates: list[CandidateRepo]) -> None:
        for c in candidates:
            if not c.readme_text:
                c.readme_text = await self._fetch_readme(c.owner, c.name)

    async def discover_all(
        self,
        known_urls: list[str] | None = None,
        fetch_readmes: bool = True,
    ) -> list[CandidateRepo]:
        all_candidates: list[CandidateRepo] = []
        all_candidates.extend(await self.search_by_topics())
        all_candidates.extend(await self.search_by_keywords())
        all_candidates.extend(await self.crawl_orgs())
        all_candidates.extend(await self.crawl_tapeout_repos())
        if known_urls:
            all_candidates.extend(await self.add_known_repos(known_urls))
        if fetch_readmes:
            await self.fetch_readmes(all_candidates)
        logger.info("Discovered %d unique repos", len(all_candidates))
        return all_candidates
