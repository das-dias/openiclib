---
title: Submitting Designs
---

# How to Submit a Design

Openiclib welcomes contributions of open-source IC designs. You can submit a
design by opening a pull request that adds an entry to `data/designs.json`.

## Requirements

Your design repository should include:

1. **A public GitHub or GitLab repository** containing the design source files.
2. **A README** with a summary of the circuit, key specifications, and the
   target PDK.
3. **Simulation or measurement results** (encouraged but not required).

## JSON Entry Format

Each design is a JSON object with the following fields:

| Field | Type | Description |
|---|---|---|
| `id` | string | Unique slug, e.g. `ihp-160ghz-lna` |
| `name` | string | Human-readable design name |
| `summary` | string | One-paragraph description (max 500 chars) |
| `source_url` | string | URL to the repo or subdirectory |
| `repo_owner` | string | GitHub/GitLab org or user |
| `repo_name` | string | Repository name |
| `pdk` | enum | `skywater130`, `ihp130sg`, `gf180`, `gf90`, `gf45`, or `unknown` |
| `circuit_class` | enum | `analog`, `digital`, `mixed-signal`, `optical`, or `unknown` |
| `circuit_type` | list | Specific types: `LNA`, `TIA`, `ADC`, `PLL`, `VCO`, etc. |
| `silicon_proven` | bool | `true` if the design has been fabricated and measured |
| `specifications` | object | Key-value pairs for specs (bandwidth, gain, etc.) |
| `tags` | list | Freeform search tags |
| `classified_by` | enum | Use `manual` for human submissions |
| `classified_at` | string | ISO 8601 timestamp |
| `readme_excerpt` | string | First ~500 chars of README |

## Classification Tags

### PDK

Use the exact enum value matching the target process:

- `skywater130` — SkyWater SKY130 (130 nm CMOS)
- `ihp130sg` — IHP SG13G2 (130 nm SiGe BiCMOS)
- `gf180` — GlobalFoundries GF180MCU (180 nm CMOS)
- `gf90` — GlobalFoundries 90 nm
- `gf45` — GlobalFoundries 45 nm
- `unknown` — PDK not identified

### Circuit Class

- `analog` — Amplifiers, filters, references, oscillators
- `digital` — Processors, logic, memory
- `mixed-signal` — ADCs, DACs, PLLs, SerDes
- `optical` — Photonic / electro-optical circuits
- `unknown` — Class not identified

### Circuit Type Examples

`LNA`, `TIA`, `PGA`, `VCO`, `PLL`, `DLL`, `ADC`, `DAC`, `Buffer`,
`Reference`, `Current Bias`, `Oscillator`, `DC-DC Converter`, `RF PA`,
`SERDES`, `Processor`, `Classifier`, `Filter`, `Mixer`

## Submission Steps

1. Fork the [openiclib repository](https://github.com/openiclib/openiclib).
2. Add your design entry to `data/designs.json`.
3. Run validation: `uv run openiclib db validate`
4. Open a pull request with a short description of the design.

The CI pipeline will automatically validate the JSON structure and run tests.
