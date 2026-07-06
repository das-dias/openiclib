from __future__ import annotations

import base64
from unittest.mock import AsyncMock

import httpx
import pytest

from openiclib.discover import GitHubDiscoverer, TapeoutSource
from openiclib.discover_gitlab import GitLabDiscoverer
from openiclib.types import CandidateRepo


def _make_github_repo(
    name: str = "test-repo",
    owner: str = "test-owner",
    **overrides,
) -> dict:
    defaults = {
        "html_url": f"https://github.com/{owner}/{name}",
        "name": name,
        "owner": {"login": owner},
        "description": f"A test repo: {name}",
        "topics": ["open-pdk"],
        "stargazers_count": 42,
        "updated_at": "2025-03-01T00:00:00Z",
    }
    defaults.update(overrides)
    return defaults


def _make_gitlab_project(
    name: str = "test-project",
    namespace: str = "test-ns",
    **overrides,
) -> dict:
    defaults = {
        "web_url": f"https://gitlab.com/{namespace}/{name}",
        "path": name,
        "namespace": {"path": namespace},
        "description": f"A test project: {name}",
        "topics": ["pdk"],
        "star_count": 10,
        "last_activity_at": "2025-03-01T00:00:00Z",
    }
    defaults.update(overrides)
    return defaults


def _mock_response(data, status_code: int = 200) -> httpx.Response:
    return httpx.Response(
        status_code=status_code,
        json=data,
        request=httpx.Request("GET", "https://example.com"),
    )


class TestGitHubDiscoverer:
    @pytest.mark.asyncio
    async def test_search_by_topics_deduplicates(self):
        repo = _make_github_repo()
        mock_resp = _mock_response({"items": [repo, repo]})

        async with GitHubDiscoverer(token="fake") as gh:
            gh._client = AsyncMock()
            gh._client.get = AsyncMock(return_value=mock_resp)
            candidates = await gh.search_by_topics()

        assert len(candidates) == 1
        assert candidates[0].url == "https://github.com/test-owner/test-repo"

    @pytest.mark.asyncio
    async def test_search_by_keywords(self):
        repo1 = _make_github_repo(name="lna-design")
        repo2 = _make_github_repo(name="adc-design", owner="other")
        mock_resp = _mock_response({"items": [repo1, repo2]})

        async with GitHubDiscoverer() as gh:
            gh._client = AsyncMock()
            gh._client.get = AsyncMock(return_value=mock_resp)
            candidates = await gh.search_by_keywords()

        assert len(candidates) == 2
        names = {c.name for c in candidates}
        assert "lna-design" in names
        assert "adc-design" in names

    @pytest.mark.asyncio
    async def test_crawl_orgs(self):
        repos = [_make_github_repo(name=f"repo-{i}") for i in range(3)]
        mock_resp = _mock_response(repos)

        async with GitHubDiscoverer() as gh:
            gh._client = AsyncMock()
            gh._client.get = AsyncMock(return_value=mock_resp)
            candidates = await gh.crawl_orgs()

        assert len(candidates) == 3

    @pytest.mark.asyncio
    async def test_fetch_readme_base64(self):
        readme_content = "# My Design\n\nA great LNA."
        encoded = base64.b64encode(readme_content.encode()).decode()
        mock_resp = _mock_response({"content": encoded, "encoding": "base64"})

        async with GitHubDiscoverer() as gh:
            gh._client = AsyncMock()
            gh._client.get = AsyncMock(return_value=mock_resp)
            text = await gh._fetch_readme("owner", "repo")

        assert text == readme_content

    @pytest.mark.asyncio
    async def test_fetch_readme_404(self):
        mock_resp = _mock_response({}, status_code=404)

        async with GitHubDiscoverer() as gh:
            gh._client = AsyncMock()
            gh._client.get = AsyncMock(return_value=mock_resp)
            text = await gh._fetch_readme("owner", "repo")

        assert text == ""

    @pytest.mark.asyncio
    async def test_rate_limit_handled(self):
        mock_resp = _mock_response({}, status_code=403)

        async with GitHubDiscoverer() as gh:
            gh._client = AsyncMock()
            gh._client.get = AsyncMock(return_value=mock_resp)
            items = await gh._search_repos("test query")

        assert items == []

    @pytest.mark.asyncio
    async def test_add_known_repos(self):
        repo = _make_github_repo(name="known-repo", owner="known-owner")
        mock_resp = _mock_response(repo)

        async with GitHubDiscoverer() as gh:
            gh._client = AsyncMock()
            gh._client.get = AsyncMock(return_value=mock_resp)
            candidates = await gh.add_known_repos(
                ["https://github.com/known-owner/known-repo"]
            )

        assert len(candidates) == 1
        assert candidates[0].name == "known-repo"

    @pytest.mark.asyncio
    async def test_candidate_fields(self):
        repo = _make_github_repo(
            name="my-lna",
            owner="chip-lab",
            description="160GHz LNA design",
            topics=["ihp-sg13g2", "lna"],
            stargazers_count=15,
        )
        mock_resp = _mock_response({"items": [repo]})

        async with GitHubDiscoverer() as gh:
            gh._client = AsyncMock()
            gh._client.get = AsyncMock(return_value=mock_resp)
            candidates = await gh.search_by_topics()

        c = candidates[0]
        assert c.owner == "chip-lab"
        assert c.name == "my-lna"
        assert c.description == "160GHz LNA design"
        assert c.topics == ["ihp-sg13g2", "lna"]
        assert c.stars == 15
        assert c.source == "github"


class TestGitLabDiscoverer:
    @pytest.mark.asyncio
    async def test_search_by_keywords(self):
        projects = [
            _make_gitlab_project(name="gl-lna"),
            _make_gitlab_project(name="gl-adc", namespace="other-ns"),
        ]
        mock_resp = _mock_response(projects)

        async with GitLabDiscoverer() as gl:
            gl._client = AsyncMock()
            gl._client.get = AsyncMock(return_value=mock_resp)
            candidates = await gl.search_by_keywords()

        assert len(candidates) == 2
        assert all(c.source == "gitlab" for c in candidates)

    @pytest.mark.asyncio
    async def test_deduplication(self):
        project = _make_gitlab_project()
        mock_resp = _mock_response([project, project])

        async with GitLabDiscoverer() as gl:
            gl._client = AsyncMock()
            gl._client.get = AsyncMock(return_value=mock_resp)
            candidates = await gl.search_by_keywords()

        assert len(candidates) == 1

    @pytest.mark.asyncio
    async def test_fetch_readme_base64(self):
        readme_content = "# GitLab Design"
        encoded = base64.b64encode(readme_content.encode()).decode()
        mock_resp = _mock_response({"content": encoded, "encoding": "base64"})

        async with GitLabDiscoverer() as gl:
            gl._client = AsyncMock()
            gl._client.get = AsyncMock(return_value=mock_resp)
            text = await gl._fetch_readme(123)

        assert text == readme_content


class TestCrawlTapeoutRepos:
    @pytest.mark.asyncio
    async def test_ihp_style_root_dirs(self):
        """IHP tapeout repos list designs at root level with README.md."""
        dir_listing = [
            {"name": "160GHz_LNA", "type": "dir"},
            {"name": "40GHz_TIA", "type": "dir"},
            {"name": "drc", "type": "dir"},
            {"name": ".github", "type": "dir"},
            {"name": "README.md", "type": "file"},
        ]
        readme_content = "# 160GHz LNA\nA low noise amplifier."
        encoded = base64.b64encode(readme_content.encode()).decode()

        async def mock_get(url, **kwargs):
            if "/contents" in url and url.endswith("/contents"):
                return _mock_response(dir_listing)
            if "160GHz_LNA/README.md" in url or "40GHz_TIA/README.md" in url:
                return _mock_response({"content": encoded, "encoding": "base64"})
            return _mock_response({}, status_code=404)

        source = TapeoutSource("IHP-GmbH", "TO_Apr2025", pdk_topic="sg13g2")

        async with GitHubDiscoverer(token="fake") as gh:
            gh._client = AsyncMock()
            gh._client.get = AsyncMock(side_effect=mock_get)
            candidates = await gh.crawl_tapeout_repos([source])

        assert len(candidates) == 2
        names = {c.name for c in candidates}
        assert "160GHz_LNA" in names
        assert "40GHz_TIA" in names
        assert "drc" not in names

        lna = next(c for c in candidates if c.name == "160GHz_LNA")
        assert "sg13g2" in lna.topics
        assert "tapeout" in lna.topics
        assert "silicon-proven" in lna.topics
        assert lna.readme_text == readme_content
        assert lna.source == "github-tapeout"
        assert "/tree/main/160GHz_LNA" in lna.url

    @pytest.mark.asyncio
    async def test_tt_style_projects_subdir(self):
        """TinyTapeout shuttle repos list projects under projects/ with info.yaml."""
        dir_listing = [
            {"name": "tt_um_my_design", "type": "dir"},
            {"name": "tt_um_factory_test", "type": "dir"},
        ]
        info_yaml = (
            "project:\n"
            "  title: My Cool Design\n"
            "  description: A digital counter\n"
        )
        encoded = base64.b64encode(info_yaml.encode()).decode()

        async def mock_get(url, **kwargs):
            if "contents/projects" in url and not url.endswith(".yaml"):
                return _mock_response(dir_listing)
            if "info.yaml" in url:
                return _mock_response({"content": encoded, "encoding": "base64"})
            return _mock_response({}, status_code=404)

        source = TapeoutSource(
            "TinyTapeout", "tinytapeout-06",
            subpath="projects", pdk_topic="sky130",
            info_file="info.yaml", extra_topics=("tinytapeout",),
        )

        async with GitHubDiscoverer(token="fake") as gh:
            gh._client = AsyncMock()
            gh._client.get = AsyncMock(side_effect=mock_get)
            candidates = await gh.crawl_tapeout_repos([source])

        assert len(candidates) == 2
        design = next(c for c in candidates if c.name == "tt_um_my_design")
        assert "sky130" in design.topics
        assert "tinytapeout" in design.topics
        assert "tapeout" in design.topics
        assert "My Cool Design" in design.description
        assert "A digital counter" in design.description
        assert "/tree/main/projects/tt_um_my_design" in design.url

    @pytest.mark.asyncio
    async def test_skip_dirs_filtering(self):
        dir_listing = [
            {"name": "design_a", "type": "dir"},
            {"name": "docs", "type": "dir"},
            {"name": "symbol", "type": "dir"},
            {"name": ".media", "type": "dir"},
        ]

        async def mock_get(url, **kwargs):
            if "/contents" in url:
                return _mock_response(dir_listing)
            return _mock_response({}, status_code=404)

        source = TapeoutSource("org", "repo", pdk_topic="sg13g2")

        async with GitHubDiscoverer() as gh:
            gh._client = AsyncMock()
            gh._client.get = AsyncMock(side_effect=mock_get)
            candidates = await gh.crawl_tapeout_repos([source])

        assert len(candidates) == 1
        assert candidates[0].name == "design_a"

    @pytest.mark.asyncio
    async def test_deduplicates_urls(self):
        dir_listing = [{"name": "design_a", "type": "dir"}]

        async def mock_get(url, **kwargs):
            if "/contents" in url:
                return _mock_response(dir_listing)
            return _mock_response({}, status_code=404)

        source = TapeoutSource("org", "repo", pdk_topic="sg13g2")

        async with GitHubDiscoverer() as gh:
            gh._client = AsyncMock()
            gh._client.get = AsyncMock(side_effect=mock_get)
            c1 = await gh.crawl_tapeout_repos([source])
            c2 = await gh.crawl_tapeout_repos([source])

        assert len(c1) == 1
        assert len(c2) == 0

    @pytest.mark.asyncio
    async def test_handles_api_failure(self):
        async with GitHubDiscoverer() as gh:
            gh._client = AsyncMock()
            gh._client.get = AsyncMock(return_value=_mock_response({}, status_code=404))
            candidates = await gh.crawl_tapeout_repos(
                [TapeoutSource("org", "repo")]
            )

        assert candidates == []

    @pytest.mark.asyncio
    async def test_parse_info_yaml(self):
        title, desc = GitHubDiscoverer._parse_info_yaml(
            "project:\n  title: My Chip\n  description: A fast ADC\n"
        )
        assert title == "My Chip"
        assert desc == "A fast ADC"

    @pytest.mark.asyncio
    async def test_parse_info_yaml_invalid(self):
        title, desc = GitHubDiscoverer._parse_info_yaml("not valid yaml: [")
        assert title == ""
        assert desc == ""


class TestCandidateRepo:
    def test_defaults(self):
        c = CandidateRepo(url="https://github.com/a/b", owner="a", name="b")
        assert c.description == ""
        assert c.readme_text == ""
        assert c.topics == []
        assert c.stars == 0
        assert c.last_updated is None
        assert c.source == "github"
