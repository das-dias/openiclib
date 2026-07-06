---
title: Examples
---

# Design Examples

This page walks through the designs currently indexed in Openiclib, showing
how each entry maps to the database schema.

## 160 GHz Low Noise Amplifier

A mm-wave LNA designed in the IHP SG13G2 BiCMOS process, part of the
IHP April 2025 tapeout run.

| Specification | Value |
|---|---|
| Bandwidth | 146 – 173 GHz (27 GHz) |
| Noise Figure | 5.77 dB @ 160 GHz |
| Peak Gain | 12.5 dB @ 157 GHz |
| Input P1dB | -11.4 dBm @ 160 GHz |

**Classification**:

- **PDK**: `ihp130sg`
- **Class**: `analog`
- **Type**: `LNA`
- **Silicon proven**: Yes
- **Tags**: mm-wave, D-band, BiCMOS, tapeout-apr2025

**Repository**: [IHP-GmbH/TO_Apr2025 — 160GHz_LNA](https://github.com/IHP-GmbH/TO_Apr2025/tree/main/160GHz_LNA)

---

## DC-40 GHz Low-Noise TIA

A broadband single-ended Transimpedance Amplifier optimized for low
input-referred current noise density, targeting optical receiver front-ends.

| Specification | Value |
|---|---|
| Bandwidth | DC to 40 GHz |
| Input Noise Density | ~9.5 pA/&radic;Hz |
| Topology | Single-ended |

**Classification**:

- **PDK**: `ihp130sg`
- **Class**: `analog`
- **Type**: `TIA`
- **Silicon proven**: Yes
- **Tags**: broadband, optical, BiCMOS, tapeout-apr2025

**Repository**: [IHP-GmbH/TO_Apr2025 — 40_GHZ_LOW_NOISE_TIA](https://github.com/IHP-GmbH/TO_Apr2025/tree/main/40_GHZ_LOW_NOISE_TIA)

---

## Using the CLI

You can explore the database from the command line:

```bash
# List all designs
uv run openiclib db list

# Validate the database
uv run openiclib db validate
```

## Running Discovery

To search GitHub and GitLab for new candidate repos:

```bash
# Dry run — print candidates without saving
uv run openiclib discover --source github --dry-run

# Save candidates to a file
uv run openiclib discover --source all --output candidates.json
```
