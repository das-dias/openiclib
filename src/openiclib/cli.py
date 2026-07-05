from __future__ import annotations

from pathlib import Path

import click

from openiclib.db import DEFAULT_DB_PATH, load_database, validate_database


@click.group()
def main() -> None:
    """Openiclib — Open Integrated Circuit Library CLI."""


@main.group()
def db() -> None:
    """Design database commands."""


@db.command("list")
@click.option("--pdk", default=None, help="Filter by PDK (e.g. ihp130sg)")
@click.option("--circuit-class", default=None, help="Filter by class")
@click.option("--proven/--unproven", default=None, help="Filter by silicon-proven")
@click.option(
    "--db-path",
    type=click.Path(exists=True, path_type=Path),
    default=DEFAULT_DB_PATH,
)
def list_designs(
    pdk: str | None,
    circuit_class: str | None,
    proven: bool | None,
    db_path: Path,
) -> None:
    """List designs in the database."""
    database = load_database(db_path)
    designs = database.filter_designs(
        pdk=pdk,
        circuit_class=circuit_class,
        silicon_proven=proven,
    )

    if not designs:
        click.echo("No designs found.")
        return

    click.echo(f"Found {len(designs)} design(s):\n")
    for d in designs:
        proven_badge = "  [silicon proven]" if d.silicon_proven else ""
        click.echo(f"  {d.id}")
        click.echo(f"    {d.name}{proven_badge}")
        types = ", ".join(d.circuit_type)
        click.echo(f"    PDK: {d.pdk}  |  Class: {d.circuit_class}  |  Type: {types}")
        if d.specifications:
            specs = ", ".join(f"{k}: {v}" for k, v in d.specifications.items())
            click.echo(f"    Specs: {specs}")
        click.echo(f"    Source: {d.source_url}")
        click.echo()


@db.command("validate")
@click.option("--db-path", type=click.Path(exists=True, path_type=Path), default=DEFAULT_DB_PATH)
def validate(db_path: Path) -> None:
    """Validate the design database."""
    errors = validate_database(db_path)
    if errors:
        click.echo("Validation errors:", err=True)
        for err in errors:
            click.echo(f"  - {err}", err=True)
        raise SystemExit(1)
    click.echo("Database is valid.")
