from __future__ import annotations

import logging
import re
from datetime import UTC, datetime

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from openiclib.models import ClassifiedBy, Design

logger = logging.getLogger(__name__)

PDK_KEYWORDS: dict[str, list[str]] = {
    "skywater130": ["sky130", "skywater", "skywater-pdk", "skywater130", "sky130-pdk"],
    "ihp130sg": ["sg13g2", "sg13s", "ihp-sg13g2", "ihp130sg", "ihp-open-pdk", "ihp130"],
    "gf180": ["gf180", "gf180mcu", "gf180mcu-pdk"],
    "gf90": ["gf90"],
    "gf45": ["gf45"],
}

CIRCUIT_TYPE_KEYWORDS: dict[str, list[str]] = {
    "LNA": ["lna", "low noise amplifier", "low-noise amplifier"],
    "TIA": ["tia", "transimpedance amplifier", "transimpedance"],
    "PGA": ["pga", "programmable gain amplifier"],
    "VCO": ["vco", "voltage controlled oscillator", "voltage-controlled oscillator"],
    "PLL": ["pll", "phase locked loop", "phase-locked loop"],
    "DLL": ["dll", "delay locked loop", "delay-locked loop"],
    "ADC": ["adc", "analog to digital", "analog-to-digital"],
    "DAC": ["dac", "digital to analog", "digital-to-analog"],
    "Buffer": ["buffer", "output buffer", "clock buffer"],
    "Reference": ["reference", "voltage reference"],
    "Current Bias": ["current bias", "current mirror", "bias generator"],
    "Oscillator": ["oscillator", "ring oscillator", "crystal oscillator"],
    "DC-DC Converter": ["dc-dc", "dc dc converter", "buck converter", "boost converter"],
    "RF PA": ["rf pa", "power amplifier rf"],
    "Power Amplifier": ["power amplifier", "pa "],
    "SERDES": ["serdes", "serializer", "deserializer"],
    "Processor": ["processor", "cpu", "microprocessor"],
    "RISC-V Core": ["risc-v", "riscv", "risc v core", "riscv core"],
    "Filter": ["filter", "low pass filter", "band pass filter", "lpf", "bpf"],
    "Mixer": ["mixer", "frequency mixer", "rf mixer"],
    "Bandgap": ["bandgap", "band gap", "bgr"],
    "OTA": ["ota", "operational transconductance"],
    "Comparator": ["comparator"],
    "LDO": ["ldo", "low dropout", "low-dropout"],
    "Charge Pump": ["charge pump"],
    "Temperature Sensor": ["temperature sensor", "temp sensor", "thermal sensor"],
    "SRAM": ["sram", "static ram"],
    "GPIO": ["gpio", "general purpose io"],
    "SoC": ["soc", "system on chip", "system-on-chip"],
    "Ring Oscillator": ["ring oscillator", "ring osc"],
    "Frequency Divider": ["frequency divider", "prescaler", "divider circuit"],
    "Regulator": ["regulator", "voltage regulator"],
    "Op-Amp": ["opamp", "op-amp", "operational amplifier"],
    "Classifier": ["classifier", "neural network accelerator"],
}

CLASS_PROTOTYPES: dict[str, str] = {
    "analog": (
        "amplifier lna tia pga vco oscillator filter mixer bandgap ota comparator "
        "ldo reference bias regulator rf power amplifier analog opamp operational "
        "transimpedance low noise wideband broadband gain noise figure"
    ),
    "digital": (
        "processor risc-v riscv sram gpio accelerator controller cpu logic memory "
        "soc digital core pipeline register alu instruction cache verilog rtl "
        "synthesis standard cell"
    ),
    "mixed-signal": (
        "adc dac pll dll serdes clock data converter charge pump frequency "
        "synthesizer mixed signal analog digital interface sigma delta sar "
        "successive approximation phase locked loop"
    ),
    "optical": (
        "photonic electro-optical optical receiver transmitter photodiode "
        "modulator waveguide silicon photonics laser detector optical"
    ),
}

SILICON_PROVEN_KEYWORDS: list[str] = [
    "tapeout", "tape-out", "tape out", "taped out", "taped-out",
    "fabricated", "fabrication", "silicon proven", "silicon-proven",
    "mpw", "shuttle", "chipignite", "chip ignite",
    "measurement results", "measured results", "chip photo",
    "die photo", "silicon measurement", "tinytapeout",
]

NEGATIVE_KEYWORDS: list[str] = [
    "process design kit", "pdk", "eda tool", "eda framework",
    "openlane", "openroad", "magic vlsi", "klayout", "yosys",
    "xschem", "netgen", "ngspice", "iverilog", "verilator",
    "cocotb", "tutorial", "course", "template", "caravel_user_project_analog",
]

NEGATIVE_NAME_PATTERNS: list[str] = [
    "pdk", "openlane", "openroad", "klayout", "yosys", "xschem",
    "netgen", "ngspice", "magic", "cocotb", "verilator", "iverilog",
    "tutorial", "course", "template", "analog-template",
]


def _combine_text(
    name: str, description: str, topics: list[str], readme_text: str
) -> str:
    parts = [name, description, " ".join(topics)]
    if readme_text:
        parts.append(readme_text[:3000])
    return " ".join(parts).lower()


def _detect_pdk(text: str, topics: list[str]) -> str:
    topics_lower = [t.lower() for t in topics]
    for pdk, keywords in PDK_KEYWORDS.items():
        for kw in keywords:
            if kw in topics_lower or kw in text:
                return pdk
    return "unknown"


def _detect_circuit_types(text: str) -> list[str]:
    text_lower = text.lower()
    found = []
    for ctype, keywords in CIRCUIT_TYPE_KEYWORDS.items():
        for kw in keywords:
            if re.search(r"\b" + re.escape(kw) + r"\b", text_lower):
                found.append(ctype)
                break
    return found or ["unknown"]


def _detect_circuit_class(text: str) -> str:
    prototypes = list(CLASS_PROTOTYPES.values())
    labels = list(CLASS_PROTOTYPES.keys())
    docs = prototypes + [text]

    vectorizer = TfidfVectorizer(stop_words="english", lowercase=True)
    tfidf_matrix = vectorizer.fit_transform(docs)

    candidate_vec = tfidf_matrix[-1:]
    proto_vecs = tfidf_matrix[:-1]
    similarities = cosine_similarity(candidate_vec, proto_vecs)[0]

    best_idx = similarities.argmax()
    if similarities[best_idx] < 0.03:
        return "unknown"
    return labels[best_idx]


def _is_silicon_proven(text: str, topics: list[str]) -> bool:
    combined = text + " " + " ".join(t.lower() for t in topics)
    return any(kw in combined for kw in SILICON_PROVEN_KEYWORDS)


def _is_design(
    text: str, name: str, topics: list[str], pdk: str, circuit_types: list[str]
) -> bool:
    topics_lower = {t.lower() for t in topics}
    if "silicon-proven" in topics_lower or "tapeout" in topics_lower:
        return True

    name_lower = name.lower()
    for pattern in NEGATIVE_NAME_PATTERNS:
        if pattern in name_lower and pdk == "unknown":
            return False

    text_lower = text.lower()
    for neg in NEGATIVE_KEYWORDS:
        if neg in text_lower:
            if circuit_types == ["unknown"]:
                return False

    has_pdk = pdk != "unknown"
    has_circuit = circuit_types != ["unknown"]

    if has_pdk and has_circuit:
        return True
    if has_circuit:
        return True
    if has_pdk:
        circuit_words = [
            "amplifier", "oscillator", "converter", "filter", "processor",
            "core", "sensor", "receiver", "transmitter", "driver", "circuit",
            "chip", "asic", "design", "layout", "schematic",
        ]
        return any(w in text_lower for w in circuit_words)
    return False


def _clean_name(owner: str, name: str) -> str:
    cleaned = name
    if cleaned.startswith("tt_um_"):
        cleaned = cleaned[6:]
    cleaned = cleaned.replace("_", " ").replace("-", " ")
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned.title()


def _extract_summary(description: str, readme_text: str) -> str:
    if description:
        return description[:500]
    if readme_text:
        for para in readme_text.split("\n\n"):
            para = para.strip()
            if not para or para.startswith("#"):
                continue
            return para[:500]
    return ""


def _slugify(owner: str, name: str) -> str:
    raw = f"{owner}-{name}".lower()
    return re.sub(r"[^a-z0-9]+", "-", raw).strip("-")[:80]


def classify_candidate(
    *,
    url: str,
    owner: str,
    name: str,
    description: str,
    topics: list[str],
    readme_text: str,
) -> Design | None:
    text = _combine_text(name, description, topics, readme_text)

    pdk = _detect_pdk(text, topics)
    circuit_types = _detect_circuit_types(text)
    circuit_class = _detect_circuit_class(text)
    silicon_proven = _is_silicon_proven(text, topics)

    if not _is_design(text, name, topics, pdk, circuit_types):
        logger.info("Skipping %s/%s — not classified as a design", owner, name)
        return None

    tags = [t for t in topics if t]
    if silicon_proven and "tapeout" not in tags:
        tags.append("tapeout")

    try:
        return Design(
            id=_slugify(owner, name),
            name=_clean_name(owner, name),
            summary=_extract_summary(description, readme_text)[:500],
            source_url=url,
            repo_owner=owner,
            repo_name=name,
            pdk=pdk,
            circuit_class=circuit_class,
            circuit_type=circuit_types,
            silicon_proven=silicon_proven,
            specifications={},
            tags=tags,
            classified_by=ClassifiedBy.KEYWORD,
            classified_at=datetime.now(UTC),
            readme_excerpt=(readme_text[:500] if readme_text else ""),
        )
    except Exception:
        logger.exception("Failed to build Design for %s/%s", owner, name)
        return None
