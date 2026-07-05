# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Openiclib is an open-source library aggregating silicon-proven, taped-out IC designs from open PDKs. It serves as a reusable IP catalog for research groups, startups, and students doing IC system-level design. The project is affiliated with gdsfactory.

## Build & Development

- **Python 3.12**, managed with **uv** (build backend: `uv_build`)
- **Docs**: MkDocs with the `shadcn` theme. Serve locally with `uv run mkdocs serve`
- **Linting**: `uv run ruff check .` (rules: E, F, I, UP; line-length 100; pdks/ excluded)
- **Tests**: `uv run pytest` (31 tests covering models and database)
- **CLI**: `uv run openiclib db list`, `uv run openiclib db validate`

## Key Commands

```bash
uv sync                      # Install all dependencies (including dev group)
uv run pytest                # Run tests
uv run ruff check .          # Lint
uv run openiclib db list     # List designs in the JSON database
uv run openiclib db validate # Validate database integrity
uv run mkdocs serve          # Serve docs locally
make init                    # Sparse-clone IHP tapeout repo + create symlinks
make update                  # Pull latest changes in the cloned tapeout repo
make clean                   # Remove clone and symlinks
```

## Architecture

### PDK design hierarchy

Designs are organized as `pdks/<foundry>/<design_name>`. The canonical structure:

```
pdks/
  ihp/
    TO_Apr2025/          # Git submodule: IHP-GmbH/TO_Apr2025 (sparse checkout)
    160GHz_LNA -> TO_Apr2025/160GHz_LNA       # symlink
    40_GHZ_LOW_NOISE_TIA -> TO_Apr2025/...    # symlink
```

- Upstream tapeout repos are sparse-cloned as git submodules under their foundry directory
- Symlinks at `pdks/<foundry>/<design>` point into the clone, giving flat access
- The Makefile manages clone, symlink, and update lifecycle

### Each circuit block should contain

- **SPICE / Verilog-A** netlists (schematic)
- **GDSII / OASIS** files (layout)
- **LVS / DRC** result databases (JSON or text)
- **Documentation**: Markdown READMEs, Jupyter notebooks with design intent

### Design database

`data/designs.json` is a flat JSON file tracking all indexed IC designs. Schema is defined by Pydantic models in `src/openiclib/models.py` (single source of truth) and exported to `data/schema.json`.

Each design is classified by:
- **PDK**: `skywater130`, `ihp130sg`, `gf180`, `gf90`, `gf45`, `unknown`
- **Circuit class**: `analog`, `digital`, `mixed-signal`, `unknown`
- **Circuit type**: free-form list (e.g. `["LNA"]`, `["ADC", "DAC"]`)
- **Silicon proven**: boolean

Key modules:
- `src/openiclib/models.py` — Pydantic models: `Design`, `DesignDatabase`, enums
- `src/openiclib/db.py` — Load/save/validate the JSON database
- `src/openiclib/cli.py` — Click CLI entry point

### Docs site

MkDocs config is in `mkdocs.yml`. Pages live in `docs/`. Uses `mkdocs-shadcn` theme with KaTeX math support and ECharts for charts.
