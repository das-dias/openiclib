# Openiclib

**Open Integrated Circuit Library** — a curated catalog of silicon-proven IC designs from open PDKs.

[![CI](https://github.com/gdsfactory/openiclib/actions/workflows/ci.yml/badge.svg)](https://github.com/gdsfactory/openiclib/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Supported PDKs](#supported-pdks)
- [Getting Started](#getting-started)
- [Usage](#usage)
  - [Browse the Library](#browse-the-library)
  - [CLI](#cli)
  - [Discovery Pipeline](#discovery-pipeline)
- [Architecture](#architecture)
- [Contributing](#contributing)
- [Citing](#citing)
- [License](#license)

---

## Overview

Openiclib aggregates taped-out, silicon-proven IC designs built on open-source process design kits (PDKs). It provides a searchable, filterable catalog that researchers, startups, and students can use as a reference library for IC system-level design.

The project automatically discovers design repositories on GitHub and GitLab, classifies them by PDK, circuit class, and circuit type using a keyword + TF-IDF classifier, and publishes the results as a browsable website with interactive statistics.

Openiclib is affiliated with [gdsfactory](https://github.com/gdsfactory/gdsfactory).

## Features

- **Automated discovery** — crawls GitHub and GitLab for IC design repos using topic search, keyword search, org crawling, and tapeout repo subdirectory enumeration
- **Keyword + TF-IDF classification** — classifies designs by PDK, circuit class (analog/digital/mixed-signal/optical), circuit type, and silicon-proven status using scikit-learn (no API keys needed)
- **Tapeout repo crawling** — enumerates individual designs inside IHP-GmbH tapeout repos and TinyTapeout shuttle repos
- **Filterable web catalog** — MkDocs-powered site with GitHub-style cards, search, dropdown filters, and silicon-proven toggle
- **Interactive statistics** — ECharts-based dashboards showing design distributions by PDK, circuit class, type, and fabrication status
- **CLI tools** — list, validate, discover, and classify designs from the command line
- **Weekly CI pipeline** — GitHub Actions workflow that discovers, classifies, and opens a PR with database updates

## Supported PDKs

| PDK | Foundry | Node |
|-----|---------|------|
| SkyWater SKY130 | SkyWater Technology | 130 nm CMOS |
| IHP SG13G2 | IHP Microelectronics | 130 nm BiCMOS |
| GlobalFoundries GF180MCU | GlobalFoundries | 180 nm CMOS |

## Getting Started

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager

### Installation

```bash
git clone https://github.com/gdsfactory/openiclib.git
cd openiclib
uv sync
```

### Quick Start

```bash
# List all designs in the database
uv run openiclib db list

# Filter by PDK
uv run openiclib db list --pdk ihp130sg

# Filter silicon-proven designs only
uv run openiclib db list --proven

# Validate the database
uv run openiclib db validate
```

## Usage

### Browse the Library

Visit the live site at **[openiclib.github.io](https://openiclib.github.io)** to browse, search, and filter designs interactively.

To serve the docs locally:

```bash
uv run mkdocs serve
```

### CLI

```bash
# List designs with filters
uv run openiclib db list --pdk skywater130 --circuit-class analog

# Validate database integrity
uv run openiclib db validate

# Discover candidate repos (dry run)
uv run openiclib discover --source github --dry-run

# Classify candidates into the design database
uv run openiclib classify --input candidates.json --output data/designs.json -v
```

### Discovery Pipeline

Run the full pipeline to discover, classify, and validate:

```bash
make pipeline
```

This executes:
1. **Discover** — searches GitHub/GitLab for IC design repos and crawls IHP + TinyTapeout tapeout directories
2. **Classify** — runs the keyword + TF-IDF classifier on all candidates
3. **Validate** — checks database integrity

Set `GITHUB_TOKEN` for higher API rate limits:

```bash
GITHUB_TOKEN=ghp_... make pipeline
```

## Architecture

```
GitHub/GitLab APIs ──→ discover.py ──→ candidates.json
                                           │
                            keyword_classifier.py (TF-IDF + scikit-learn)
                                           │
                                      designs.json
                                           │
                            catalog_hook.py (MkDocs on_pre_build)
                             │          │           │
                        library.md   stats.md   designs.json
                             │
                        MkDocs build ──→ GitHub Pages
```

### Key Modules

| Module | Purpose |
|--------|---------|
| `models.py` | Pydantic data models (`Design`, `DesignDatabase`, enums) |
| `db.py` | Load/save/validate JSON database + protobuf conversion |
| `discover.py` | GitHub discovery (topics, keywords, orgs, tapeout repos) |
| `discover_gitlab.py` | GitLab discovery |
| `keyword_classifier.py` | TF-IDF + keyword classification (scikit-learn) |
| `cli.py` | Click CLI (`db list`, `db validate`, `discover`, `classify`) |
| `stats.py` | Statistics generation |
| `catalog_hook.py` | MkDocs hook generating library and stats pages |

### Design Database

The canonical database is `data/designs.json`. Each design is classified by:

- **PDK**: skywater130, ihp130sg, gf180, gf90, gf45
- **Circuit class**: analog, digital, mixed-signal, optical
- **Circuit type**: LNA, ADC, PLL, RISC-V Core, SoC, etc.
- **Silicon proven**: fabricated and measured

The protobuf schema in `data/designs.proto` serves as the formal schema definition.

## Contributing

Contributions are welcome! You can:

1. **Submit a design** — open a PR adding your design to `data/designs.json`
2. **Improve classification** — add keywords to `keyword_classifier.py` for better accuracy
3. **Add discovery sources** — extend `discover.py` with new orgs, topics, or tapeout repos
4. **Report issues** — [open an issue](https://github.com/gdsfactory/openiclib/issues) for bugs or feature requests

### Development

```bash
uv sync                      # Install dependencies
uv run pytest                # Run tests (116 tests)
uv run ruff check .          # Lint
uv run mkdocs build --strict # Build docs
```

## Citing

If you use Openiclib in your research, please cite:

```bibtex
@software{dias2026openiclib,
  author       = {Dias, Diogo},
  title        = {Openiclib: Open Integrated Circuit Library},
  year         = {2026},
  url          = {https://github.com/das-dias/openiclib},
  license      = {MIT},
  note         = {A searchable catalog of silicon-proven IC designs from open PDKs (SKY130, IHP SG13G2, GF180)}
}
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
