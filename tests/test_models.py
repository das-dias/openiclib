from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from openiclib.models import (
    PDK,
    CircuitClass,
    ClassifiedBy,
    Design,
    DesignDatabase,
)


def _make_design(**overrides):
    defaults = {
        "id": "test-design",
        "name": "Test Design",
        "summary": "A test design",
        "source_url": "https://github.com/test/repo",
        "repo_owner": "test",
        "repo_name": "repo",
        "pdk": PDK.IHP130SG,
        "circuit_class": CircuitClass.ANALOG,
        "circuit_type": ["LNA"],
        "silicon_proven": True,
        "classified_by": ClassifiedBy.MANUAL,
        "classified_at": datetime(2025, 1, 1, tzinfo=UTC),
    }
    defaults.update(overrides)
    return Design(**defaults)


class TestPDKEnum:
    def test_all_pdks(self):
        assert set(PDK) == {
            PDK.SKYWATER130,
            PDK.IHP130SG,
            PDK.GF180,
            PDK.GF90,
            PDK.GF45,
            PDK.UNKNOWN,
        }

    def test_string_values(self):
        assert PDK.SKYWATER130 == "skywater130"
        assert PDK.IHP130SG == "ihp130sg"


class TestCircuitClassEnum:
    def test_all_classes(self):
        assert set(CircuitClass) == {
            CircuitClass.ANALOG,
            CircuitClass.DIGITAL,
            CircuitClass.MIXED_SIGNAL,
            CircuitClass.OPTICAL,
            CircuitClass.UNKNOWN,
        }

    def test_mixed_signal_value(self):
        assert CircuitClass.MIXED_SIGNAL == "mixed-signal"


class TestDesign:
    def test_create_minimal(self):
        d = _make_design()
        assert d.id == "test-design"
        assert d.specifications == {}
        assert d.tags == []
        assert d.local_path is None
        assert d.readme_excerpt == ""

    def test_create_with_specs(self):
        d = _make_design(specifications={"gain": "12 dB", "bandwidth": "10 GHz"})
        assert d.specifications["gain"] == "12 dB"

    def test_invalid_pdk_rejected(self):
        with pytest.raises(ValidationError):
            _make_design(pdk="invalid_pdk")

    def test_invalid_circuit_class_rejected(self):
        with pytest.raises(ValidationError):
            _make_design(circuit_class="not-a-class")

    def test_summary_max_length(self):
        with pytest.raises(ValidationError):
            _make_design(summary="x" * 501)

    def test_roundtrip_json(self):
        d = _make_design(specifications={"gain": "12 dB"}, tags=["test"])
        json_str = d.model_dump_json()
        d2 = Design.model_validate_json(json_str)
        assert d == d2


class TestDesignDatabase:
    def _make_db(self, designs=None):
        return DesignDatabase(
            generated_at=datetime(2025, 1, 1, tzinfo=UTC),
            designs=designs or [],
        )

    def test_empty_database(self):
        db = self._make_db()
        assert len(db.designs) == 0
        assert db.version == "1.0.0"

    def test_find_by_id(self):
        d = _make_design(id="lna-1")
        db = self._make_db([d])
        assert db.find_by_id("lna-1") == d
        assert db.find_by_id("nonexistent") is None

    def test_find_by_source_url(self):
        d = _make_design(source_url="https://github.com/test/repo")
        db = self._make_db([d])
        assert db.find_by_source_url("https://github.com/test/repo") == d
        assert db.find_by_source_url("https://other.com") is None

    def test_filter_by_pdk(self):
        d1 = _make_design(id="d1", pdk=PDK.IHP130SG)
        d2 = _make_design(id="d2", pdk=PDK.SKYWATER130, source_url="https://other.com")
        db = self._make_db([d1, d2])
        results = db.filter_designs(pdk=PDK.IHP130SG)
        assert len(results) == 1
        assert results[0].id == "d1"

    def test_filter_by_circuit_class(self):
        d1 = _make_design(id="d1", circuit_class=CircuitClass.ANALOG)
        d2 = _make_design(
            id="d2",
            circuit_class=CircuitClass.DIGITAL,
            source_url="https://other.com",
        )
        db = self._make_db([d1, d2])
        results = db.filter_designs(circuit_class=CircuitClass.DIGITAL)
        assert len(results) == 1
        assert results[0].id == "d2"

    def test_filter_by_silicon_proven(self):
        d1 = _make_design(id="d1", silicon_proven=True)
        d2 = _make_design(id="d2", silicon_proven=False, source_url="https://other.com")
        db = self._make_db([d1, d2])
        assert len(db.filter_designs(silicon_proven=True)) == 1
        assert len(db.filter_designs(silicon_proven=False)) == 1

    def test_filter_by_circuit_type(self):
        d1 = _make_design(id="d1", circuit_type=["LNA"])
        d2 = _make_design(id="d2", circuit_type=["ADC", "DAC"], source_url="https://other.com")
        db = self._make_db([d1, d2])
        assert len(db.filter_designs(circuit_type="LNA")) == 1
        assert len(db.filter_designs(circuit_type="adc")) == 1  # case-insensitive
        assert len(db.filter_designs(circuit_type="PLL")) == 0

    def test_roundtrip_json(self):
        d = _make_design()
        db = self._make_db([d])
        json_str = db.model_dump_json()
        db2 = DesignDatabase.model_validate_json(json_str)
        assert db == db2
