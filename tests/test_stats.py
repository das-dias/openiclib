from __future__ import annotations

from datetime import UTC, datetime

from openiclib.models import (
    PDK,
    CircuitClass,
    ClassifiedBy,
    Design,
    DesignDatabase,
)
from openiclib.stats import (
    class_distribution,
    pdk_distribution,
    silicon_proven_counts,
    summary,
    type_distribution,
)


def _make_design(
    *,
    id_: str = "test",
    pdk: PDK = PDK.IHP130SG,
    circuit_class: CircuitClass = CircuitClass.ANALOG,
    circuit_type: list[str] | None = None,
    silicon_proven: bool = True,
) -> Design:
    return Design(
        id=id_,
        name=f"Design {id_}",
        summary="Test design",
        source_url=f"https://github.com/test/{id_}",
        repo_owner="test",
        repo_name=id_,
        pdk=pdk,
        circuit_class=circuit_class,
        circuit_type=["LNA"] if circuit_type is None else circuit_type,
        silicon_proven=silicon_proven,
        classified_by=ClassifiedBy.MANUAL,
        classified_at=datetime(2025, 1, 1, tzinfo=UTC),
    )


def _make_db(*designs: Design) -> DesignDatabase:
    return DesignDatabase(
        generated_at=datetime(2025, 1, 1, tzinfo=UTC),
        designs=list(designs),
    )


def test_pdk_distribution_single():
    db = _make_db(_make_design(id_="a"), _make_design(id_="b"))
    dist = pdk_distribution(db)
    assert dist == {"ihp130sg": 2}


def test_pdk_distribution_multiple():
    db = _make_db(
        _make_design(id_="a", pdk=PDK.IHP130SG),
        _make_design(id_="b", pdk=PDK.SKYWATER130),
        _make_design(id_="c", pdk=PDK.SKYWATER130),
    )
    dist = pdk_distribution(db)
    assert dist == {"ihp130sg": 1, "skywater130": 2}


def test_class_distribution():
    db = _make_db(
        _make_design(id_="a", circuit_class=CircuitClass.ANALOG),
        _make_design(id_="b", circuit_class=CircuitClass.DIGITAL),
        _make_design(id_="c", circuit_class=CircuitClass.ANALOG),
    )
    dist = class_distribution(db)
    assert dist == {"analog": 2, "digital": 1}


def test_type_distribution():
    db = _make_db(
        _make_design(id_="a", circuit_type=["LNA"]),
        _make_design(id_="b", circuit_type=["LNA", "TIA"]),
    )
    dist = type_distribution(db)
    assert dist == {"LNA": 2, "TIA": 1}


def test_type_distribution_empty():
    db = _make_db(_make_design(id_="a", circuit_type=[]))
    dist = type_distribution(db)
    assert dist == {}


def test_silicon_proven_counts():
    db = _make_db(
        _make_design(id_="a", silicon_proven=True),
        _make_design(id_="b", silicon_proven=False),
        _make_design(id_="c", silicon_proven=True),
    )
    counts = silicon_proven_counts(db)
    assert counts == {"Silicon Proven": 2, "Unverified": 1}


def test_silicon_proven_all_proven():
    db = _make_db(_make_design(id_="a"), _make_design(id_="b"))
    counts = silicon_proven_counts(db)
    assert counts == {"Silicon Proven": 2, "Unverified": 0}


def test_summary_keys():
    db = _make_db(_make_design())
    s = summary(db)
    assert set(s.keys()) == {"total_designs", "by_pdk", "by_class", "by_type", "by_proven"}
    assert s["total_designs"] == 1


def test_empty_database():
    db = _make_db()
    assert pdk_distribution(db) == {}
    assert class_distribution(db) == {}
    assert type_distribution(db) == {}
    assert silicon_proven_counts(db) == {"Silicon Proven": 0, "Unverified": 0}
    assert summary(db)["total_designs"] == 0
