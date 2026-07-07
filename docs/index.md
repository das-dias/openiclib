# OpenIClib

## Open Integrated Circuit Library

**A curated catalog of silicon-proven IC designs from open PDKs — for researchers, startups, and students doing IC system-level design.**

Openiclib aggregates taped-out, silicon-proven IC designs built on open-source process design kits (PDKs). It provides a searchable, filterable catalog that you can use as a reference library when designing integrated circuits.

The project automatically discovers design repositories on GitHub and GitLab, classifies them by PDK, circuit class, and circuit type using a keyword + TF-IDF classifier, and publishes the results here as a browsable website with interactive statistics.

Openiclib is affiliated with [gdsfactory](https://github.com/gdsfactory/gdsfactory).

## Features

- **Automated discovery** — crawls GitHub and GitLab for IC design repos using topic search, keyword search, org crawling, and tapeout repo subdirectory enumeration
- **Keyword + TF-IDF classification** — classifies designs by PDK, circuit class, circuit type, and silicon-proven status (no API keys needed)
- **Tapeout repo crawling** — enumerates individual designs inside IHP-GmbH tapeout repos and TinyTapeout shuttle repos
- **Filterable web catalog** — browse the [Library](library.md) with search, dropdown filters, and silicon-proven toggle
- **Interactive statistics** — [Stats](stats.md) dashboards showing design distributions by PDK, circuit class, type, and fabrication status
- **CLI tools** — list, validate, discover, and classify designs from the command line

## Supported PDKs

| PDK | Foundry | Node |
|-----|---------|------|
| SkyWater SKY130 | SkyWater Technology | 130 nm CMOS |
| IHP SG13G2 | IHP Microelectronics | 130 nm BiCMOS |
| GlobalFoundries GF180MCU | GlobalFoundries | 180 nm CMOS |

## Getting Started

```bash
git clone https://github.com/das-dias/openiclib.git
cd openiclib
uv sync
uv run openiclib db list
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
