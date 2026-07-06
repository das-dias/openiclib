# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Openiclib is an open-source library aggregating silicon-proven, taped-out IC designs from open PDKs. It serves as a reusable IP catalog for research groups, startups, and students doing IC system-level design. The project is affiliated with gdsfactory.

## Build & Development

- **Python 3.12**, managed with **uv** (build backend: `uv_build`)
- **Docs**: MkDocs with the `shadcn` theme. Serve locally with `uv run mkdocs serve`
- **Linting**: `uv run ruff check .` (rules: E, F, I, UP; line-length 100; hooks/, *_pb2.py excluded)
- **Tests**: `uv run pytest` (116 tests covering models, database, discovery, classification, stats, and catalog hook)
- **CLI**: `uv run openiclib db list`, `uv run openiclib db validate`

## Key Commands

```bash
uv sync                      # Install all dependencies (including dev group)
uv run pytest                # Run all tests
uv run pytest tests/test_models.py::TestDesign::test_create_minimal  # Run a single test
uv run pytest -k "roundtrip" # Run tests matching keyword
uv run ruff check .          # Lint
uv run openiclib db list     # List designs in the JSON database
uv run openiclib db validate # Validate database integrity
uv run openiclib discover --source github --dry-run  # Preview discovered repos
uv run mkdocs serve          # Serve docs locally
uv run mkdocs build --strict # Build docs (used in CI)
make pipeline                # Full discover → classify → validate pipeline
make docs                    # Build MkDocs site
```

Recompile protobuf after editing `data/designs.proto`:

```bash
uv run python -m grpc_tools.protoc -I data --python_out=src/openiclib --pyi_out=src/openiclib data/designs.proto
```

## Architecture

### Data pipeline

```
GitHub/GitLab APIs → discover.py → candidates.json
                                       ↓
                          keyword_classifier.py (TF-IDF + scikit-learn)
                                       ↓
                                  designs.json
                                       ↓
                          catalog_hook.py (on_pre_build)
                           ↓           ↓            ↓
                     library.md    stats.md    assets/designs.json
                           ↓
                      MkDocs build → GitHub Pages
```

### Design database

`data/designs.json` is the canonical JSON database. Protobuf schema in `data/designs.proto` serves as the formal schema (replaces the former `schema.json`). Pydantic models in `src/openiclib/models.py` are the single source of truth for the Python layer, with bidirectional protobuf conversion in `db.py`.

Each design is classified by:
- **PDK**: `skywater130`, `ihp130sg`, `gf180`, `gf90`, `gf45`, `unknown`
- **Circuit class**: `analog`, `digital`, `mixed-signal`, `optical`, `unknown`
- **Circuit type**: free-form list (e.g. `["LNA"]`, `["ADC", "DAC"]`)
- **Silicon proven**: boolean

### Key modules

- `src/openiclib/models.py` — Pydantic models: `Design`, `DesignDatabase`, enums (`PDK`, `CircuitClass`, `ClassifiedBy`)
- `src/openiclib/db.py` — Load/save/validate JSON database + protobuf conversion. `DEFAULT_DB_PATH` resolves to `data/designs.json`
- `src/openiclib/cli.py` — Click CLI: `db list`, `db validate`, `discover`
- `src/openiclib/discover.py` — GitHub repo discovery (async, httpx): topics, keywords, org crawl, known repos
- `src/openiclib/discover_gitlab.py` — GitLab repo discovery (same pattern)
- `src/openiclib/types.py` — `CandidateRepo` dataclass
- `src/openiclib/keyword_classifier.py` — Classify candidates using TF-IDF + keyword matching (scikit-learn, no API key needed)
- `src/openiclib/stats.py` — Statistics generation (Counter-based distributions by PDK, class, type, proven)
- `hooks/catalog_hook.py` — MkDocs `on_pre_build` hook generating `library.md`, `stats.md`, and `assets/designs.json`

### Generated vs checked-in files

These files are **generated at build time** by the catalog hook and gitignored — do not edit them directly:
- `docs/library.md`, `docs/stats.md`, `docs/assets/designs.json`

### Docs site

MkDocs config is in `mkdocs.yml`. Uses `mkdocs-shadcn` theme with KaTeX math, ECharts charts (`shadcn.extensions.echarts.alpha`), and client-side JS filtering for the library page (`docs/assets/catalog.js` + `docs/assets/catalog.css`).
