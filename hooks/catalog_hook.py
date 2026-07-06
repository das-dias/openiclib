from __future__ import annotations

import json
from html import escape
from pathlib import Path

from mkdocs.config.defaults import MkDocsConfig


def on_pre_build(*, config: MkDocsConfig) -> None:
    db_path = Path(config.docs_dir).parent / "data" / "designs.json"
    if not db_path.exists():
        return

    with open(db_path) as f:
        db = json.load(f)

    designs = db.get("designs", [])

    catalog_path = Path(config.docs_dir) / "catalog.md"
    catalog_path.write_text(_render_catalog(designs))

    assets_dir = Path(config.docs_dir) / "assets"
    assets_dir.mkdir(exist_ok=True)
    (assets_dir / "designs.json").write_text(json.dumps(db, indent=2))


def _render_catalog(designs: list[dict]) -> str:
    pdk_options = sorted({d["pdk"] for d in designs})
    class_options = sorted({d["circuit_class"] for d in designs})
    type_options = sorted({t for d in designs for t in d.get("circuit_type", [])})

    parts = [
        "---",
        "title: Catalog",
        "---",
        "",
        "# Design Catalog",
        "",
        '<div class="catalog-controls">',
        '  <input type="text" id="filter-search" placeholder="Search designs..." class="catalog-search">',
        '  <div class="catalog-filters">',
        _select("filter-pdk", "All PDKs", pdk_options),
        _select("filter-class", "All Classes", class_options),
        _select("filter-type", "All Types", type_options),
        '    <label class="catalog-toggle">',
        '      <input type="checkbox" id="filter-proven">',
        "      Silicon proven only",
        "    </label>",
        "  </div>",
        '</div>',
        "",
        '<p id="catalog-count" class="catalog-count"></p>',
        "",
        '<div class="catalog-grid" id="catalog-grid">',
    ]

    for d in designs:
        parts.append(_render_card(d))

    parts.append("</div>")
    return "\n".join(parts) + "\n"


def _select(id_: str, placeholder: str, options: list[str]) -> str:
    opts = [f'    <option value="all">{placeholder}</option>']
    for o in options:
        label = o.replace("-", " ").replace("_", " ").title()
        opts.append(f'    <option value="{escape(o)}">{escape(label)}</option>')
    return f'    <select id="{id_}" class="catalog-select">\n' + "\n".join(opts) + "\n    </select>"


def _render_card(d: dict) -> str:
    esc = escape
    types_str = ", ".join(d.get("circuit_type", []))
    data_types = " ".join(d.get("circuit_type", []))
    proven = "true" if d.get("silicon_proven") else "false"
    name = esc(d.get("name", ""))
    summary = esc(d.get("summary", ""))
    pdk = d.get("pdk", "unknown")
    circuit_class = d.get("circuit_class", "unknown")
    source_url = esc(d.get("source_url", ""))

    pdk_label = pdk.replace("-", " ").replace("_", " ").title()
    class_label = circuit_class.replace("-", " ").replace("_", " ").title()

    specs_html = ""
    specs = d.get("specifications", {})
    if specs:
        items = "".join(
            f'<span class="card-spec">{esc(k.replace("_", " "))}: {esc(v)}</span>'
            for k, v in specs.items()
        )
        specs_html = f'<div class="card-specs">{items}</div>'

    proven_badge = ""
    if d.get("silicon_proven"):
        proven_badge = '<span class="badge badge-proven">Silicon Proven</span>'

    repo_owner = esc(d.get("repo_owner", ""))
    repo_name = esc(d.get("repo_name", ""))
    repo_label = f"{repo_owner}/{repo_name}" if repo_owner else repo_name

    return f"""\
<div class="design-card"
     data-pdk="{esc(pdk)}"
     data-class="{esc(circuit_class)}"
     data-types="{esc(data_types)}"
     data-proven="{proven}"
     data-name="{name.lower()}">
  <div class="card-header">
    <h3><a href="{source_url}" target="_blank" rel="noopener">{name}</a></h3>
    {proven_badge}
  </div>
  <p class="card-summary">{summary}</p>
  <div class="card-badges">
    <span class="badge badge-pdk">{esc(pdk_label)}</span>
    <span class="badge badge-class">{esc(class_label)}</span>
    <span class="badge badge-type">{esc(types_str)}</span>
  </div>
  {specs_html}
  <div class="card-footer">
    <a href="{source_url}" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> {repo_label}</a>
  </div>
</div>"""
