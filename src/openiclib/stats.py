from __future__ import annotations

from collections import Counter

from openiclib.models import DesignDatabase


def pdk_distribution(db: DesignDatabase) -> dict[str, int]:
    return dict(Counter(d.pdk.value for d in db.designs))


def class_distribution(db: DesignDatabase) -> dict[str, int]:
    return dict(Counter(d.circuit_class.value for d in db.designs))


def type_distribution(db: DesignDatabase) -> dict[str, int]:
    return dict(Counter(t for d in db.designs for t in d.circuit_type))


def silicon_proven_counts(db: DesignDatabase) -> dict[str, int]:
    proven = sum(1 for d in db.designs if d.silicon_proven)
    return {"Silicon Proven": proven, "Unverified": len(db.designs) - proven}


def summary(db: DesignDatabase) -> dict:
    return {
        "total_designs": len(db.designs),
        "by_pdk": pdk_distribution(db),
        "by_class": class_distribution(db),
        "by_type": type_distribution(db),
        "by_proven": silicon_proven_counts(db),
    }
