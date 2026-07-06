from __future__ import annotations

import base64
import logging
from datetime import datetime
from urllib.parse import quote_plus

import httpx

from openiclib.types import CandidateRepo

logger = logging.getLogger(__name__)

KEYWORD_QUERIES = [
    "tapeout pdk",
    "silicon proven pdk",
    "open pdk amplifier",
    "ASIC LNA OR TIA OR ADC",
    "skywater OR gf180 OR ihp pdk",
]

API_BASE = "https://gitlab.com/api/v4"
RESULTS_PER_PAGE = 20
MAX_PAGES_PER_QUERY = 3


class GitLabDiscoverer:
    def __init__(self, token: str | None = None) -> None:
        headers: dict[str, str] = {}
        if token:
            headers["PRIVATE-TOKEN"] = token
        self._client = httpx.AsyncClient(
            base_url=API_BASE,
            headers=headers,
            timeout=30.0,
        )
        self._seen: set[str] = set()

    async def __aenter__(self) -> GitLabDiscoverer:
        return self

    async def __aexit__(self, *exc) -> None:
        await self._client.aclose()

    async def _search_projects(self, query: str) -> list[dict]:
        results: list[dict] = []
        for page in range(1, MAX_PAGES_PER_QUERY + 1):
            resp = await self._client.get(
                "/projects",
                params={
                    "search": query,
                    "visibility": "public",
                    "per_page": RESULTS_PER_PAGE,
                    "page": page,
                    "order_by": "stars",
                },
            )
            if resp.status_code != 200:
                logger.warning("GitLab search failed for %r: %d", query, resp.status_code)
                break
            items = resp.json()
            results.extend(items)
            if len(items) < RESULTS_PER_PAGE:
                break
        return results

    async def _fetch_readme(self, project_id: int) -> str:
        encoded = quote_plus("README.md")
        resp = await self._client.get(
            f"/projects/{project_id}/repository/files/{encoded}",
            params={"ref": "main"},
        )
        if resp.status_code != 200:
            resp = await self._client.get(
                f"/projects/{project_id}/repository/files/{encoded}",
                params={"ref": "master"},
            )
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

    def _project_to_candidate(self, item: dict, readme: str = "") -> CandidateRepo:
        updated = item.get("last_activity_at")
        web_url = item.get("web_url", "")
        namespace = item.get("namespace", {})
        return CandidateRepo(
            url=web_url,
            owner=namespace.get("path", ""),
            name=item.get("path", ""),
            description=item.get("description") or "",
            readme_text=readme,
            topics=item.get("topics", []),
            stars=item.get("star_count", 0),
            last_updated=datetime.fromisoformat(updated) if updated else None,
            source="gitlab",
        )

    async def search_by_keywords(self) -> list[CandidateRepo]:
        candidates: list[CandidateRepo] = []
        for kw in KEYWORD_QUERIES:
            logger.info("Searching GitLab: %s", kw)
            items = await self._search_projects(kw)
            for item in items:
                url = item.get("web_url", "")
                if url in self._seen:
                    continue
                self._seen.add(url)
                candidates.append(self._project_to_candidate(item))
        return candidates

    async def fetch_readmes(self, candidates: list[CandidateRepo]) -> None:
        for c in candidates:
            if not c.readme_text and c.url:
                resp = await self._client.get(
                    "/projects",
                    params={"search": c.name, "visibility": "public", "per_page": 1},
                )
                if resp.status_code == 200 and resp.json():
                    project_id = resp.json()[0].get("id")
                    if project_id:
                        c.readme_text = await self._fetch_readme(project_id)

    async def discover_all(self, fetch_readmes: bool = True) -> list[CandidateRepo]:
        candidates = await self.search_by_keywords()
        if fetch_readmes:
            await self.fetch_readmes(candidates)
        logger.info("Discovered %d unique GitLab repos", len(candidates))
        return candidates
