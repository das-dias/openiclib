from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

from google.protobuf import timestamp_pb2

from openiclib.designs_pb2 import (
    CIRCUIT_CLASS_ANALOG,
    CIRCUIT_CLASS_DIGITAL,
    CIRCUIT_CLASS_MIXED_SIGNAL,
    CIRCUIT_CLASS_OPTICAL,
    CIRCUIT_CLASS_UNKNOWN,
    CLASSIFIED_BY_LLM_CLAUDE,
    CLASSIFIED_BY_LLM_GITHUB_MODELS,
    CLASSIFIED_BY_LLM_OLLAMA,
    CLASSIFIED_BY_MANUAL,
    CLASSIFIED_BY_UNSPECIFIED,
    PDK_GF45,
    PDK_GF90,
    PDK_GF180,
    PDK_IHP130SG,
    PDK_SKYWATER130,
    PDK_UNKNOWN,
)
from openiclib.designs_pb2 import Design as DesignProto
from openiclib.designs_pb2 import DesignDatabase as DesignDatabaseProto
from openiclib.models import PDK, CircuitClass, ClassifiedBy, Design, DesignDatabase

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DB_PATH = _PROJECT_ROOT / "data" / "designs.json"

_PDK_TO_PROTO = {
    PDK.SKYWATER130: PDK_SKYWATER130,
    PDK.IHP130SG: PDK_IHP130SG,
    PDK.GF180: PDK_GF180,
    PDK.GF90: PDK_GF90,
    PDK.GF45: PDK_GF45,
    PDK.UNKNOWN: PDK_UNKNOWN,
}
_PDK_FROM_PROTO = {v: k for k, v in _PDK_TO_PROTO.items()}

_CLASS_TO_PROTO = {
    CircuitClass.ANALOG: CIRCUIT_CLASS_ANALOG,
    CircuitClass.DIGITAL: CIRCUIT_CLASS_DIGITAL,
    CircuitClass.MIXED_SIGNAL: CIRCUIT_CLASS_MIXED_SIGNAL,
    CircuitClass.OPTICAL: CIRCUIT_CLASS_OPTICAL,
    CircuitClass.UNKNOWN: CIRCUIT_CLASS_UNKNOWN,
}
_CLASS_FROM_PROTO = {v: k for k, v in _CLASS_TO_PROTO.items()}

_CLASSIFIED_TO_PROTO = {
    ClassifiedBy.MANUAL: CLASSIFIED_BY_MANUAL,
    ClassifiedBy.LLM_GITHUB_MODELS: CLASSIFIED_BY_LLM_GITHUB_MODELS,
    ClassifiedBy.LLM_CLAUDE: CLASSIFIED_BY_LLM_CLAUDE,
    ClassifiedBy.LLM_OLLAMA: CLASSIFIED_BY_LLM_OLLAMA,
}
_CLASSIFIED_FROM_PROTO = {v: k for k, v in _CLASSIFIED_TO_PROTO.items()}
_CLASSIFIED_FROM_PROTO[CLASSIFIED_BY_UNSPECIFIED] = ClassifiedBy.MANUAL


def _datetime_to_timestamp(dt: datetime) -> timestamp_pb2.Timestamp:
    ts = timestamp_pb2.Timestamp()
    ts.FromDatetime(dt)
    return ts


def _timestamp_to_datetime(ts: timestamp_pb2.Timestamp) -> datetime:
    return ts.ToDatetime(tzinfo=UTC)


def design_to_proto(d: Design) -> DesignProto:
    proto = DesignProto(
        id=d.id,
        name=d.name,
        summary=d.summary,
        source_url=d.source_url,
        repo_owner=d.repo_owner,
        repo_name=d.repo_name,
        pdk=_PDK_TO_PROTO[d.pdk],
        circuit_class=_CLASS_TO_PROTO[d.circuit_class],
        circuit_type=d.circuit_type,
        silicon_proven=d.silicon_proven,
        specifications=d.specifications,
        tags=d.tags,
        classified_by=_CLASSIFIED_TO_PROTO[d.classified_by],
        classified_at=_datetime_to_timestamp(d.classified_at),
        readme_excerpt=d.readme_excerpt,
    )
    if d.local_path is not None:
        proto.local_path = d.local_path
    return proto


def design_from_proto(proto: DesignProto) -> Design:
    return Design(
        id=proto.id,
        name=proto.name,
        summary=proto.summary,
        source_url=proto.source_url,
        repo_owner=proto.repo_owner,
        repo_name=proto.repo_name,
        pdk=_PDK_FROM_PROTO[proto.pdk],
        circuit_class=_CLASS_FROM_PROTO[proto.circuit_class],
        circuit_type=list(proto.circuit_type),
        silicon_proven=proto.silicon_proven,
        specifications=dict(proto.specifications),
        tags=list(proto.tags),
        classified_by=_CLASSIFIED_FROM_PROTO[proto.classified_by],
        classified_at=_timestamp_to_datetime(proto.classified_at),
        local_path=proto.local_path if proto.HasField("local_path") else None,
        readme_excerpt=proto.readme_excerpt,
    )


def db_to_proto(db: DesignDatabase) -> DesignDatabaseProto:
    return DesignDatabaseProto(
        version=db.version,
        generated_at=_datetime_to_timestamp(db.generated_at),
        designs=[design_to_proto(d) for d in db.designs],
    )


def db_from_proto(proto: DesignDatabaseProto) -> DesignDatabase:
    return DesignDatabase(
        version=proto.version,
        generated_at=_timestamp_to_datetime(proto.generated_at),
        designs=[design_from_proto(d) for d in proto.designs],
    )


def load_database(path: Path = DEFAULT_DB_PATH) -> DesignDatabase:
    with open(path) as f:
        return DesignDatabase.model_validate_json(f.read())


def save_database(db: DesignDatabase, path: Path = DEFAULT_DB_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        f.write(db.model_dump_json(indent=2))
        f.write("\n")


def load_database_proto(path: Path) -> DesignDatabase:
    """Load a database from a binary protobuf file."""
    proto = DesignDatabaseProto()
    proto.ParseFromString(path.read_bytes())
    return db_from_proto(proto)


def save_database_proto(db: DesignDatabase, path: Path) -> None:
    """Save the database as a binary protobuf file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(db_to_proto(db).SerializeToString())


def validate_database(path: Path = DEFAULT_DB_PATH) -> list[str]:
    """Validate the database file against the protobuf schema. Returns a list of errors."""
    errors: list[str] = []
    if not path.exists():
        return [f"Database file not found: {path}"]

    try:
        db = load_database(path)
    except Exception as e:
        return [f"Failed to parse database: {e}"]

    for design in db.designs:
        try:
            design_to_proto(design)
        except (KeyError, ValueError) as e:
            errors.append(f"Design '{design.id}' fails proto schema: {e}")

    seen_ids: set[str] = set()
    seen_urls: set[str] = set()
    for design in db.designs:
        if design.id in seen_ids:
            errors.append(f"Duplicate design ID: {design.id}")
        seen_ids.add(design.id)

        if design.source_url in seen_urls:
            errors.append(f"Duplicate source URL: {design.source_url}")
        seen_urls.add(design.source_url)

        if not design.circuit_type:
            errors.append(f"Design '{design.id}' has no circuit_type")

    return errors
