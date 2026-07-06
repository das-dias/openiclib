from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import MagicMock

from hooks.catalog_hook import on_pre_build


def _setup_env(tmp_path: Path) -> tuple[Path, MagicMock]:
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    db = {
        "version": "1.0.0",
        "generated_at": "2025-01-01T00:00:00Z",
        "designs": [
            {
                "id": "test-lna",
                "name": "Test LNA",
                "summary": "A test amplifier",
                "source_url": "https://github.com/org/repo",
                "repo_owner": "org",
                "repo_name": "repo",
                "pdk": "ihp130sg",
                "circuit_class": "analog",
                "circuit_type": ["LNA"],
                "silicon_proven": True,
                "specifications": {"gain": "10 dB"},
                "tags": ["test"],
                "classified_by": "manual",
                "classified_at": "2025-01-01T00:00:00Z",
                "readme_excerpt": "Test readme",
            }
        ],
    }
    (data_dir / "designs.json").write_text(json.dumps(db))

    config = MagicMock()
    config.docs_dir = str(docs_dir)
    return docs_dir, config


def test_generates_catalog(tmp_path):
    docs_dir, config = _setup_env(tmp_path)
    on_pre_build(config=config)

    catalog = docs_dir / "library.md"
    assert catalog.exists()
    content = catalog.read_text()
    assert "Test LNA" in content
    assert "design-card" in content
    assert "filter-pdk" in content


def test_generates_stats(tmp_path):
    docs_dir, config = _setup_env(tmp_path)
    on_pre_build(config=config)

    stats = docs_dir / "stats.md"
    assert stats.exists()
    content = stats.read_text()
    assert "Design Statistics" in content
    assert "echarts" in content
    assert "Designs by PDK" in content


def test_generates_designs_json(tmp_path):
    docs_dir, config = _setup_env(tmp_path)
    on_pre_build(config=config)

    designs_json = docs_dir / "assets" / "designs.json"
    assert designs_json.exists()
    data = json.loads(designs_json.read_text())
    assert len(data["designs"]) == 1


def test_card_has_source_link(tmp_path):
    docs_dir, config = _setup_env(tmp_path)
    on_pre_build(config=config)

    content = (docs_dir / "library.md").read_text()
    assert 'href="https://github.com/org/repo"' in content
    assert "org/repo" in content


def test_card_has_badges(tmp_path):
    docs_dir, config = _setup_env(tmp_path)
    on_pre_build(config=config)

    content = (docs_dir / "library.md").read_text()
    assert "badge-pdk" in content
    assert "badge-class" in content
    assert "badge-proven" in content


def test_card_has_specs(tmp_path):
    docs_dir, config = _setup_env(tmp_path)
    on_pre_build(config=config)

    content = (docs_dir / "library.md").read_text()
    assert "card-spec" in content
    assert "gain" in content
    assert "10 dB" in content


def test_stats_charts_present(tmp_path):
    docs_dir, config = _setup_env(tmp_path)
    on_pre_build(config=config)

    content = (docs_dir / "stats.md").read_text()
    assert "Designs by Circuit Class" in content
    assert "Designs by Circuit Type" in content
    assert "Silicon Proven Status" in content


def test_no_db_file(tmp_path):
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    config = MagicMock()
    config.docs_dir = str(docs_dir)

    on_pre_build(config=config)
    assert not (docs_dir / "library.md").exists()
    assert not (docs_dir / "stats.md").exists()


def test_empty_designs(tmp_path):
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    db = {"version": "1.0.0", "generated_at": "2025-01-01T00:00:00Z", "designs": []}
    (data_dir / "designs.json").write_text(json.dumps(db))

    config = MagicMock()
    config.docs_dir = str(docs_dir)
    on_pre_build(config=config)

    assert (docs_dir / "library.md").exists()
    assert (docs_dir / "stats.md").exists()
    content = (docs_dir / "stats.md").read_text()
    assert "**0** designs" in content
