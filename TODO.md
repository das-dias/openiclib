# TODO — Openiclib Design Discovery & Catalog

Each milestone produces one commit.

---

## Milestone 1: JSON Schema, Database, CLI & CI Scaffold

- [x] Define Pydantic models (`src/openiclib/models.py`): `Design`, `DesignDatabase`, enums for PDK, CircuitClass, CircuitType
- [x] Create `src/openiclib/db.py`: load/save/validate `data/designs.json`
- [x] Compile protobuf schema (`data/designs.proto`) — replaces JSON schema as canonical schema
- [x] Seed `data/designs.json` with 2 manually classified IHP designs (160GHz LNA, 40GHz TIA)
- [x] Create Click CLI (`src/openiclib/cli.py`): `openiclib db list`, `openiclib db validate`
- [x] Update `pyproject.toml`: add pydantic, click, protobuf, pytest, ruff; add `[project.scripts]` entry
- [x] Write tests: `tests/test_models.py`, `tests/test_db.py`
- [x] Create `.github/workflows/ci.yml`: checkout → uv sync → ruff check → pytest → mkdocs build

---

## Milestone 2: GitHub/GitLab Discovery Pipeline

- [x] Create `src/openiclib/types.py`: `CandidateRepo` dataclass
- [x] Create `src/openiclib/discover.py`: `GitHubDiscoverer` (httpx, async) — topic search, keyword search, org crawl, README extraction
- [x] Create `src/openiclib/discover_gitlab.py`: `GitLabDiscoverer` with same interface
- [x] Curate `data/known_repos.txt` with known IC design repos (IHP-GmbH, efabless, etc.)
- [x] Extend CLI: `openiclib discover --source github [--dry-run] --output candidates.json`
- [x] Update `pyproject.toml`: add httpx, pytest-asyncio dependency
- [x] Write tests: `tests/test_discover.py` with mocked HTTP responses (12 tests)
- [ ] Tune discovery queries for higher precision:
  - Add PDK-specific topics: `sg13g2`, `gf180mcu-pdk`, `sky130-pdk`, `open-source-asic`
  - Add circuit-type keyword queries: `"VCO" OR "DCO" pdk`, `"SERDES" open-source`, `"DC-DC converter" tapeout`, `"PLL" silicon`
  - Add foundry-specific orgs: `SiLabs`, `TinyTapeout`, `zerotoasiccourse`
  - Add language filters to keyword queries (e.g. `language:verilog`, `language:spice`) to reduce false positives
  - Move queries to a configurable YAML/TOML file (`data/discovery_queries.yml`) so they can be tuned without code changes
  - Add negative filters to exclude common false positives (e.g. pure-software repos, documentation-only repos)

---

## ~~Milestone 3: LLM Classification Pipeline~~ (skipped)

---

## Milestone 3: MkDocs Catalog Page with Filterable Cards

- [x] Create `hooks/catalog_hook.py`: MkDocs `on_pre_build` hook — reads `data/designs.json`, writes `docs/catalog.md` with GitHub-style card grid + filter controls
- [x] Create `docs/assets/catalog.js`: client-side filtering (PDK, circuit class, circuit type dropdowns; silicon-proven toggle; text search)
- [x] Create `docs/assets/catalog.css`: GitHub-style card layout with shadcn CSS variable fallbacks
- [x] Update `mkdocs.yml`: add `hooks:`, `extra_javascript`, `extra_css`, nav with Catalog page
- [x] Each card shows: linked title, summary, PDK/class/type badges, specs, repo link with icon

---

## Milestone 4: Stats Dashboard, Docs Content & Deploy Pipeline

- [ ] Extend `hooks/catalog_hook.py` to also generate `stats.md` with ECharts blocks (distribution by PDK, circuit class, circuit type, silicon-proven)
- [ ] Create `src/openiclib/stats.py`: generate stats dicts from `DesignDatabase`
- [ ] Fill `docs/technologies.md`: supported PDKs with links to foundry docs
- [ ] Fill `docs/submitting.md`: how to submit designs, required file formats, classification tags
- [ ] Fill `docs/examples.md`: walkthrough of IHP designs, how to use the library
- [ ] Create `.github/workflows/deploy.yml`: on push to main → mkdocs build → GitHub Pages
- [ ] Polish `.github/workflows/classify.yml`: PR creation instead of direct push, validation step
- [ ] Write tests: `tests/test_stats.py`, `tests/test_catalog_hook.py`
