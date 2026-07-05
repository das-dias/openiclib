# TODO — Openiclib Design Discovery & Catalog

Each milestone produces one commit.

---

## Milestone 1: JSON Schema, Database, CLI & CI Scaffold

- [ ] Define Pydantic models (`src/openiclib/models.py`): `Design`, `DesignDatabase`, enums for PDK (`skywater130`, `ihp130sg`, `gf180`, `gf90`, `gf45`), CircuitClass (`analog`, `digital`, `mixed-signal`), CircuitType
- [ ] Create `src/openiclib/db.py`: load/save/validate `data/designs.json`
- [ ] Export JSON Schema from Pydantic models to `data/schema.json`
- [ ] Seed `data/designs.json` with 2 manually classified IHP designs (160GHz LNA, 40GHz TIA)
- [ ] Create Click CLI (`src/openiclib/cli.py`): `openiclib db list`, `openiclib db validate`
- [ ] Update `pyproject.toml`: add pydantic, click, pytest, ruff; add `[project.scripts]` entry
- [ ] Write tests: `tests/test_models.py`, `tests/test_db.py`
- [ ] Create `.github/workflows/ci.yml`: checkout → uv sync → ruff check → pytest → mkdocs build

---

## Milestone 2: GitHub/GitLab Discovery Pipeline

- [ ] Create `src/openiclib/types.py`: `CandidateRepo` dataclass
- [ ] Create `src/openiclib/discover.py`: `GitHubDiscoverer` (httpx, async) — topic search, keyword search, org crawl, README extraction
- [ ] Create `src/openiclib/discover_gitlab.py`: `GitLabDiscoverer` with same interface
- [ ] Curate `data/known_repos.txt` with known IC design repos (IHP-GmbH, efabless, etc.)
- [ ] Extend CLI: `openiclib discover --source github [--dry-run] --output candidates.json`
- [ ] Update `pyproject.toml`: add httpx dependency
- [ ] Write tests: `tests/test_discover.py` with mocked HTTP responses

---

## Milestone 3: LLM Classification Pipeline

- [ ] Create `src/openiclib/llm.py`: `LLMBackend` protocol + `GitHubModelsBackend` (primary, uses `GITHUB_TOKEN` via Azure AI inference), `AnthropicBackend`, `OllamaBackend`
- [ ] Create `src/openiclib/prompts.py`: system prompt with classification taxonomy, few-shot examples from M1 seed data
- [ ] Create `src/openiclib/classify.py`: takes `CandidateRepo` → LLM → `Design`, merge logic
- [ ] Extend CLI: `openiclib classify --input candidates.json --backend github-models --merge data/designs.json`
- [ ] Update `pyproject.toml`: add `azure-ai-inference`; optional dep group `[anthropic]`
- [ ] Write tests: `tests/test_classify.py` with mocked LLM responses
- [ ] Create `.github/workflows/classify.yml`: weekly cron + manual dispatch → discover → classify → open PR

---

## Milestone 4: MkDocs Catalog Page with Filterable Cards

- [ ] Create `hooks/catalog_hook.py`: MkDocs hook (`on_files`) — reads `data/designs.json`, generates `catalog.md` with HTML card grid + filter controls
- [ ] Create `docs/assets/catalog.js`: client-side filtering (PDK, circuit class, circuit type dropdowns; silicon-proven toggle; text search)
- [ ] Create `docs/assets/catalog.css`: card grid layout using shadcn CSS variables (light/dark compatible)
- [ ] Update `mkdocs.yml`: add `hooks:`, `extra_javascript`, `extra_css`, nav entry for Catalog
- [ ] Verify: `mkdocs serve` shows catalog with working filters, correct card count, dark mode

---

## Milestone 5: Stats Dashboard, Docs Content & Deploy Pipeline

- [ ] Extend `hooks/catalog_hook.py` to also generate `stats.md` with ECharts blocks (distribution by PDK, circuit class, circuit type, silicon-proven)
- [ ] Create `src/openiclib/stats.py`: generate stats dicts from `DesignDatabase`
- [ ] Fill `docs/technologies.md`: supported PDKs with links to foundry docs
- [ ] Fill `docs/submitting.md`: how to submit designs, required file formats, classification tags
- [ ] Fill `docs/examples.md`: walkthrough of IHP designs, how to use the library
- [ ] Create `.github/workflows/deploy.yml`: on push to main → mkdocs build → GitHub Pages
- [ ] Polish `.github/workflows/classify.yml`: PR creation instead of direct push, validation step
- [ ] Write tests: `tests/test_stats.py`, `tests/test_catalog_hook.py`
