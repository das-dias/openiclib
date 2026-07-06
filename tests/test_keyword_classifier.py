from __future__ import annotations

from openiclib.keyword_classifier import (
    _clean_name,
    _detect_circuit_class,
    _detect_circuit_types,
    _detect_pdk,
    _extract_summary,
    _is_design,
    _is_silicon_proven,
    _slugify,
    classify_candidate,
)
from openiclib.models import ClassifiedBy


class TestDetectPDK:
    def test_sky130_in_topics(self):
        assert _detect_pdk("", ["sky130", "analog"]) == "skywater130"

    def test_ihp_in_text(self):
        assert _detect_pdk("designed in sg13g2 process", []) == "ihp130sg"

    def test_gf180_in_topics(self):
        assert _detect_pdk("", ["gf180mcu"]) == "gf180"

    def test_skywater_pdk_topic(self):
        assert _detect_pdk("", ["skywater-pdk"]) == "skywater130"

    def test_no_match(self):
        assert _detect_pdk("some random project", ["python", "ai"]) == "unknown"

    def test_ihp_in_description(self):
        assert _detect_pdk("ihp-sg13g2 bicmos technology", []) == "ihp130sg"


class TestDetectCircuitTypes:
    def test_lna(self):
        assert "LNA" in _detect_circuit_types("low noise amplifier design")

    def test_adc(self):
        assert "ADC" in _detect_circuit_types("analog to digital converter")

    def test_pll(self):
        assert "PLL" in _detect_circuit_types("phase locked loop implementation")

    def test_multiple_types(self):
        types = _detect_circuit_types("design with lna and pll blocks")
        assert "LNA" in types
        assert "PLL" in types

    def test_no_match(self):
        assert _detect_circuit_types("random software project") == ["unknown"]

    def test_case_insensitive(self):
        assert "VCO" in _detect_circuit_types("A VCO design for 5 GHz")

    def test_riscv(self):
        types = _detect_circuit_types("risc-v processor core")
        assert "RISC-V Core" in types or "Processor" in types


class TestDetectCircuitClass:
    def test_analog(self):
        assert _detect_circuit_class("amplifier lna noise figure gain") == "analog"

    def test_digital(self):
        assert _detect_circuit_class("processor risc-v core pipeline register") == "digital"

    def test_mixed_signal(self):
        assert _detect_circuit_class("adc dac converter sigma delta") == "mixed-signal"

    def test_unknown(self):
        assert _detect_circuit_class("random unrelated text with no circuit keywords") == "unknown"


class TestIsSiliconProven:
    def test_tapeout_keyword(self):
        assert _is_silicon_proven("this design was taped out", []) is True

    def test_mpw_keyword(self):
        assert _is_silicon_proven("submitted to mpw-1 shuttle", []) is True

    def test_fabrication_keyword(self):
        assert _is_silicon_proven("", ["fabrication"]) is True

    def test_no_keywords(self):
        assert _is_silicon_proven("a simulation-only design", []) is False


class TestIsDesign:
    def test_has_pdk_and_circuit(self):
        assert _is_design("lna sky130", "lna-sky130", [], "skywater130", ["LNA"]) is True

    def test_eda_tool(self):
        assert _is_design("openlane flow", "openlane", [], "unknown", ["unknown"]) is False

    def test_circuit_only(self):
        assert _is_design("adc design", "my-adc", [], "unknown", ["ADC"]) is True

    def test_no_signals(self):
        assert _is_design("python library", "mylib", [], "unknown", ["unknown"]) is False

    def test_pdk_with_design_words(self):
        text = "sky130 circuit layout"
        assert _is_design(text, "my-chip", [], "skywater130", ["unknown"]) is True

    def test_tapeout_topic_always_design(self):
        result = _is_design("", "anything", ["tapeout", "silicon-proven"], "unknown", ["unknown"])
        assert result is True


class TestCleanName:
    def test_underscores(self):
        assert _clean_name("org", "160GHz_LNA") == "160Ghz Lna"

    def test_hyphens(self):
        assert _clean_name("org", "my-cool-chip") == "My Cool Chip"

    def test_already_clean(self):
        assert _clean_name("org", "MyChip") == "Mychip"

    def test_tt_um_prefix_stripped(self):
        result = _clean_name("TinyTapeout", "tt_um_kianV_rv32ima_uLinux_SoC")
        assert result == "Kianv Rv32Ima Ulinux Soc"


class TestExtractSummary:
    def test_description(self):
        assert _extract_summary("A great design", "") == "A great design"

    def test_readme_fallback(self):
        assert _extract_summary("", "# Title\n\nFirst paragraph.") == "First paragraph."

    def test_empty(self):
        assert _extract_summary("", "") == ""

    def test_truncation(self):
        long = "A" * 600
        assert len(_extract_summary(long, "")) == 500


class TestSlugify:
    def test_basic(self):
        assert _slugify("IHP-GmbH", "TO_Apr2025") == "ihp-gmbh-to-apr2025"

    def test_special_chars(self):
        assert _slugify("org", "my repo!") == "org-my-repo"


class TestClassifyCandidate:
    def test_classifies_design(self):
        design = classify_candidate(
            url="https://github.com/test/lna-sky130",
            owner="test",
            name="lna-sky130",
            description="A low noise amplifier in sky130",
            topics=["sky130", "lna", "analog"],
            readme_text="This is a low noise amplifier designed in SKY130 PDK.",
        )
        assert design is not None
        assert design.pdk == "skywater130"
        assert "LNA" in design.circuit_type
        assert design.circuit_class == "analog"
        assert design.classified_by == ClassifiedBy.KEYWORD
        assert design.source_url == "https://github.com/test/lna-sky130"

    def test_rejects_pdk_repo(self):
        design = classify_candidate(
            url="https://github.com/google/skywater-pdk",
            owner="google",
            name="skywater-pdk",
            description="Open source process design kit for SkyWater 130nm",
            topics=["pdk", "skywater", "open-source"],
            readme_text="The SkyWater Open Source PDK is a process design kit...",
        )
        assert design is None

    def test_rejects_eda_tool(self):
        design = classify_candidate(
            url="https://github.com/The-OpenROAD-Project/OpenLane",
            owner="The-OpenROAD-Project",
            name="OpenLane",
            description="OpenLane is an automated RTL to GDSII flow",
            topics=["openlane", "eda", "asic"],
            readme_text="OpenLane is an automated RTL to GDSII flow...",
        )
        assert design is None

    def test_silicon_proven_detection(self):
        design = classify_candidate(
            url="https://github.com/test/tapeout-adc",
            owner="test",
            name="tapeout-adc",
            description="A 12-bit ADC taped out in GF180",
            topics=["gf180mcu", "tapeout", "adc"],
            readme_text="This ADC was fabricated and measured.",
        )
        assert design is not None
        assert design.silicon_proven is True
        assert design.pdk == "gf180"
        assert "ADC" in design.circuit_type

    def test_no_readme(self):
        design = classify_candidate(
            url="https://github.com/test/vco",
            owner="test",
            name="vco",
            description="Voltage controlled oscillator in sky130",
            topics=["sky130"],
            readme_text="",
        )
        assert design is not None
        assert "VCO" in design.circuit_type
