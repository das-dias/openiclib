from __future__ import annotations

import base64
import logging
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
]

API_BASE = "https://api.github.com"
RESULTS_PER_PAGE = 30
MAX_PAGES_PER_QUERY = 3


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
        resp = await self._client.get(f"/repos/{owner}/{repo}/readme")
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
        if known_urls:
            all_candidates.extend(await self.add_known_repos(known_urls))
        if fetch_readmes:
            await self.fetch_readmes(all_candidates)
        logger.info("Discovered %d unique repos", len(all_candidates))
        return all_candidates
