from __future__ import annotations

import asyncio
import dataclasses
import json
import logging
import os
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


_KNOWN_REPOS_PATH = Path(__file__).resolve().parents[2] / "data" / "known_repos.txt"


@main.command()
@click.option(
    "--source",
    type=click.Choice(["github", "gitlab", "all"]),
    default="all",
    help="Which platform(s) to search",
)
@click.option(
    "--output",
    type=click.Path(path_type=Path),
    default="data/candidates.json",
    help="Output path for candidates JSON",
)
@click.option("--dry-run", is_flag=True, help="Print results without writing")
@click.option("-v", "--verbose", is_flag=True, help="Enable verbose logging")
def discover(source: str, output: Path, dry_run: bool, verbose: bool) -> None:
    """Discover IC design repos on GitHub and GitLab."""
    if verbose:
        logging.basicConfig(level=logging.INFO)

    asyncio.run(_discover_async(source, output, dry_run))


async def _discover_async(source: str, output: Path, dry_run: bool) -> None:
    from openiclib.discover import GitHubDiscoverer
    from openiclib.discover_gitlab import GitLabDiscoverer
    from openiclib.types import CandidateRepo

    known_urls: list[str] = []
    if _KNOWN_REPOS_PATH.exists():
        known_urls = [
            line.strip()
            for line in _KNOWN_REPOS_PATH.read_text().splitlines()
            if line.strip() and not line.startswith("#")
        ]

    all_candidates: list[CandidateRepo] = []
    token = os.environ.get("GITHUB_TOKEN")

    if source in ("github", "all"):
        async with GitHubDiscoverer(token=token) as gh:
            all_candidates.extend(await gh.discover_all(known_urls=known_urls))

    if source in ("gitlab", "all"):
        gitlab_token = os.environ.get("GITLAB_TOKEN")
        async with GitLabDiscoverer(token=gitlab_token) as gl:
            all_candidates.extend(await gl.discover_all())

    # Dedup across sources by URL
    seen: set[str] = set()
    deduped: list[CandidateRepo] = []
    for c in all_candidates:
        if c.url not in seen:
            seen.add(c.url)
            deduped.append(c)

    click.echo(f"Discovered {len(deduped)} unique repo(s)")

    if dry_run:
        for c in deduped:
            star_str = f"  ({c.stars} stars)" if c.stars else ""
            click.echo(f"  {c.url}{star_str}")
            if c.description:
                click.echo(f"    {c.description[:100]}")
        return

    data = [dataclasses.asdict(c) for c in deduped]
    for item in data:
        if item.get("last_updated"):
            item["last_updated"] = item["last_updated"].isoformat()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, indent=2) + "\n")
    click.echo(f"Written to {output}")
