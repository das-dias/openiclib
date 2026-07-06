from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class CandidateRepo:
    url: str
    owner: str
    name: str
    description: str = ""
    readme_text: str = ""
    topics: list[str] = field(default_factory=list)
    stars: int = 0
    last_updated: datetime | None = None
    source: str = "github"
