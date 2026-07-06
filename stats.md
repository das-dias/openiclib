---
title: Stats
---

# Design Statistics

**122** designs indexed across **4** PDK technologies.

## Distribution by PDK

/// echarts
{
  "title": {
    "text": "Designs by PDK",
    "left": "center"
  },
  "tooltip": {
    "trigger": "item"
  },
  "series": [
    {
      "type": "pie",
      "radius": "65%",
      "data": [
        {
          "name": "Ihp130Sg",
          "value": 25
        },
        {
          "name": "Skywater130",
          "value": 49
        },
        {
          "name": "Gf180",
          "value": 6
        },
        {
          "name": "Unknown",
          "value": 42
        }
      ],
      "emphasis": {
        "itemStyle": {
          "shadowBlur": 10,
          "shadowOffsetX": 0,
          "shadowColor": "rgba(0, 0, 0, 0.5)"
        }
      }
    }
  ]
}
///

## Distribution by Circuit Class

/// echarts
{
  "title": {
    "text": "Designs by Circuit Class",
    "left": "center"
  },
  "tooltip": {
    "trigger": "item"
  },
  "series": [
    {
      "type": "pie",
      "radius": "65%",
      "data": [
        {
          "name": "Analog",
          "value": 15
        },
        {
          "name": "Digital",
          "value": 68
        },
        {
          "name": "Unknown",
          "value": 11
        },
        {
          "name": "Mixed Signal",
          "value": 9
        },
        {
          "name": "Optical",
          "value": 19
        }
      ],
      "emphasis": {
        "itemStyle": {
          "shadowBlur": 10,
          "shadowOffsetX": 0,
          "shadowColor": "rgba(0, 0, 0, 0.5)"
        }
      }
    }
  ]
}
///

## Circuit Types

/// echarts
{
  "title": {
    "text": "Designs by Circuit Type",
    "left": "center"
  },
  "tooltip": {
    "trigger": "axis"
  },
  "xAxis": {
    "type": "category",
    "data": [
      "unknown",
      "SoC",
      "RISC-V Core",
      "Processor",
      "SRAM",
      "LDO",
      "DAC",
      "Filter",
      "ADC",
      "Oscillator",
      "LNA",
      "OTA",
      "Op-Amp",
      "Reference",
      "VCO",
      "SERDES",
      "TIA",
      "Regulator",
      "Bandgap",
      "Power Amplifier",
      "Frequency Divider",
      "GPIO"
    ],
    "axisLabel": {
      "rotate": 30
    }
  },
  "yAxis": {
    "type": "value",
    "minInterval": 1
  },
  "series": [
    {
      "type": "bar",
      "data": [
        34,
        30,
        27,
        22,
        6,
        4,
        4,
        4,
        3,
        3,
        2,
        2,
        2,
        2,
        2,
        2,
        1,
        1,
        1,
        1,
        1,
        1
      ]
    }
  ]
}
///

## Silicon Proven

/// echarts
{
  "title": {
    "text": "Silicon Proven Status",
    "left": "center"
  },
  "tooltip": {
    "trigger": "item"
  },
  "series": [
    {
      "type": "pie",
      "radius": "65%",
      "data": [
        {
          "name": "Silicon Proven",
          "value": 34
        },
        {
          "name": "Unverified",
          "value": 88
        }
      ],
      "emphasis": {
        "itemStyle": {
          "shadowBlur": 10,
          "shadowOffsetX": 0,
          "shadowColor": "rgba(0, 0, 0, 0.5)"
        }
      }
    }
  ]
}
///

