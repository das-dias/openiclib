from datetime import UTC, datetime
from pathlib import Path

import pytest

from openiclib.db import (
    db_from_proto,
    db_to_proto,
    design_from_proto,
    design_to_proto,
    load_database,
    load_database_proto,
    save_database,
    save_database_proto,
    validate_database,
)
from openiclib.models import (
    PDK,
    CircuitClass,
    ClassifiedBy,
    Design,
    DesignDatabase,
)


@pytest.fixture
def sample_design():
    return Design(
        id="test-lna",
        name="Test LNA",
        summary="A test LNA design",
        source_url="https://github.com/test/lna",
        repo_owner="test",
        repo_name="lna",
        pdk=PDK.IHP130SG,
        circuit_class=CircuitClass.ANALOG,
        circuit_type=["LNA"],
        silicon_proven=True,
        classified_by=ClassifiedBy.MANUAL,
        classified_at=datetime(2025, 1, 1, tzinfo=UTC),
    )


@pytest.fixture
def sample_db(sample_design):
    return DesignDatabase(
        generated_at=datetime(2025, 1, 1, tzinfo=UTC),
        designs=[sample_design],
    )


class TestSaveLoad:
    def test_roundtrip(self, tmp_path, sample_db):
        db_path = tmp_path / "designs.json"
        save_database(sample_db, db_path)
        loaded = load_database(db_path)
        assert loaded == sample_db

    def test_creates_parent_dirs(self, tmp_path, sample_db):
        db_path = tmp_path / "nested" / "dir" / "designs.json"
        save_database(sample_db, db_path)
        assert db_path.exists()

    def test_load_nonexistent_raises(self, tmp_path):
        with pytest.raises(FileNotFoundError):
            load_database(tmp_path / "nonexistent.json")


class TestProtobufRoundtrip:
    def test_design_roundtrip(self, sample_design):
        proto = design_to_proto(sample_design)
        restored = design_from_proto(proto)
        assert restored == sample_design

    def test_design_with_optional_local_path(self, sample_design):
        d = sample_design.model_copy(update={"local_path": "pdks/ihp/lna"})
        proto = design_to_proto(d)
        restored = design_from_proto(proto)
        assert restored.local_path == "pdks/ihp/lna"

    def test_design_without_local_path(self, sample_design):
        proto = design_to_proto(sample_design)
        restored = design_from_proto(proto)
        assert restored.local_path is None

    def test_db_roundtrip(self, sample_db):
        proto = db_to_proto(sample_db)
        restored = db_from_proto(proto)
        assert restored == sample_db

    def test_binary_save_load(self, tmp_path, sample_db):
        proto_path = tmp_path / "designs.pb"
        save_database_proto(sample_db, proto_path)
        loaded = load_database_proto(proto_path)
        assert loaded == sample_db

    def test_all_pdks_map(self):
        for pdk in PDK:
            d = Design(
                id="t", name="t", summary="t",
                source_url="https://x.com", repo_owner="o", repo_name="r",
                pdk=pdk, circuit_class=CircuitClass.ANALOG,
                circuit_type=["X"], silicon_proven=False,
                classified_by=ClassifiedBy.MANUAL,
                classified_at=datetime(2025, 1, 1, tzinfo=UTC),
            )
            assert design_from_proto(design_to_proto(d)).pdk == pdk

    def test_all_circuit_classes_map(self):
        for cc in CircuitClass:
            d = Design(
                id="t", name="t", summary="t",
                source_url="https://x.com", repo_owner="o", repo_name="r",
                pdk=PDK.UNKNOWN, circuit_class=cc,
                circuit_type=["X"], silicon_proven=False,
                classified_by=ClassifiedBy.MANUAL,
                classified_at=datetime(2025, 1, 1, tzinfo=UTC),
            )
            assert design_from_proto(design_to_proto(d)).circuit_class == cc

    def test_all_classified_by_map(self):
        for cb in ClassifiedBy:
            d = Design(
                id="t", name="t", summary="t",
                source_url="https://x.com", repo_owner="o", repo_name="r",
                pdk=PDK.UNKNOWN, circuit_class=CircuitClass.UNKNOWN,
                circuit_type=["X"], silicon_proven=False,
                classified_by=cb,
                classified_at=datetime(2025, 1, 1, tzinfo=UTC),
            )
            assert design_from_proto(design_to_proto(d)).classified_by == cb


class TestValidateDatabase:
    def test_valid_db(self, tmp_path, sample_db):
        db_path = tmp_path / "designs.json"
        save_database(sample_db, db_path)
        errors = validate_database(db_path)
        assert errors == []

    def test_nonexistent_file(self, tmp_path):
        errors = validate_database(tmp_path / "missing.json")
        assert len(errors) == 1
        assert "not found" in errors[0]

    def test_invalid_json(self, tmp_path):
        db_path = tmp_path / "bad.json"
        db_path.write_text("not valid json")
        errors = validate_database(db_path)
        assert len(errors) == 1
        assert "Failed to parse" in errors[0]

    def test_duplicate_ids(self, tmp_path, sample_design):
        d2 = sample_design.model_copy(update={"source_url": "https://other.com"})
        db = DesignDatabase(
            generated_at=datetime(2025, 1, 1, tzinfo=UTC),
            designs=[sample_design, d2],
        )
        db_path = tmp_path / "designs.json"
        save_database(db, db_path)
        errors = validate_database(db_path)
        assert any("Duplicate design ID" in e for e in errors)

    def test_duplicate_urls(self, tmp_path, sample_design):
        d2 = sample_design.model_copy(update={"id": "different-id"})
        db = DesignDatabase(
            generated_at=datetime(2025, 1, 1, tzinfo=UTC),
            designs=[sample_design, d2],
        )
        db_path = tmp_path / "designs.json"
        save_database(db, db_path)
        errors = validate_database(db_path)
        assert any("Duplicate source URL" in e for e in errors)

    def test_empty_circuit_type(self, tmp_path, sample_design):
        d = sample_design.model_copy(update={"circuit_type": []})
        db = DesignDatabase(
            generated_at=datetime(2025, 1, 1, tzinfo=UTC),
            designs=[d],
        )
        db_path = tmp_path / "designs.json"
        save_database(db, db_path)
        errors = validate_database(db_path)
        assert any("no circuit_type" in e for e in errors)


class TestSeededDatabase:
    def test_load_seeded_db(self):
        db_path = Path(__file__).resolve().parents[1] / "data" / "designs.json"
        if not db_path.exists():
            pytest.skip("Seeded database not found")
        db = load_database(db_path)
        assert len(db.designs) >= 2

    def test_seeded_db_valid(self):
        db_path = Path(__file__).resolve().parents[1] / "data" / "designs.json"
        if not db_path.exists():
            pytest.skip("Seeded database not found")
        errors = validate_database(db_path)
        assert errors == []
