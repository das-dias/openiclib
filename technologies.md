---
title: Technologies
---

# Supported PDK Technologies

Openiclib indexes designs targeting the following open-source Process Design Kits.

## IHP SG13G2 (130 nm SiGe BiCMOS)

IHP's SG13G2 is a 130 nm SiGe BiCMOS technology offering HBTs with
*f*~T~ / *f*~max~ above 350 / 450 GHz, making it well suited to mm-wave and
high-speed analog circuits.

- **Foundry**: IHP Microelectronics, Frankfurt (Oder), Germany
- **Node**: 130 nm BiCMOS
- **Key features**: SiGe HBTs, MIM capacitors, thick-metal inductors, MOS devices
- **PDK repo**: [IHP-Open-PDK on GitHub](https://github.com/IHP-GmbH/IHP-Open-PDK)
- **Tapeout program**: [IHP Open MPW & Tapeout Runs](https://github.com/IHP-GmbH)

## SkyWater SKY130 (130 nm CMOS)

The SkyWater SKY130 is the first foundry-provided, fully open-source PDK.
It targets digital, analog, and mixed-signal designs at the 130 nm node.

- **Foundry**: SkyWater Technology, Bloomington, MN, USA
- **Node**: 130 nm CMOS (5 metal, 1 MiM cap, 1 PIP cap)
- **Key features**: Digital standard cells, I/O, SRAM, analog devices
- **PDK repo**: [google/skywater-pdk](https://github.com/google/skywater-pdk)
- **Shuttle program**: [Efabless chipIgnite](https://efabless.com)

## GlobalFoundries GF180MCU (180 nm CMOS)

GF180MCU is GlobalFoundries' open-source 180 nm MCU process, supporting
3.3 V and 6 V devices — a good fit for power management and mixed-signal ICs.

- **Foundry**: GlobalFoundries
- **Node**: 180 nm CMOS
- **Key features**: 3.3 V / 6 V devices, MIM caps, high-res resistors
- **PDK repo**: [google/gf180mcu-pdk](https://github.com/google/gf180mcu-pdk)

## GlobalFoundries GF 90 nm & 45 nm

These nodes are included for indexing completeness. Open-source PDK support
for GF 90 nm and 45 nm is limited, but select educational and research
designs target these processes.

- **GF 90 nm**: General-purpose bulk CMOS
- **GF 45 nm**: Low-power SOI CMOS (educational kits available through MUSE program)
