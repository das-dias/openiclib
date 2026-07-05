from __future__ import annotations

from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field


class PDK(StrEnum):
    SKYWATER130 = "skywater130"
    IHP130SG = "ihp130sg"
    GF180 = "gf180"
    GF90 = "gf90"
    GF45 = "gf45"
    UNKNOWN = "unknown"


class CircuitClass(StrEnum):
    ANALOG = "analog"
    DIGITAL = "digital"
    MIXED_SIGNAL = "mixed-signal"
    OPTICAL = "optical"
    UNKNOWN = "unknown"


class ClassifiedBy(StrEnum):
    MANUAL = "manual"
    LLM_GITHUB_MODELS = "llm-github-models"
    LLM_CLAUDE = "llm-claude"
    LLM_OLLAMA = "llm-ollama"


class Design(BaseModel):
    id: str = Field(description="Slugified unique ID, e.g. ihp-160ghz-lna")
    name: str
    summary: str = Field(max_length=500)
    source_url: str = Field(description="URL to the source repository or directory")
    repo_owner: str
    repo_name: str
    pdk: PDK
    circuit_class: CircuitClass
    circuit_type: list[str] = Field(
        description="Specific circuit types, e.g. ['LNA'], ['ADC', 'DAC']"
    )
    silicon_proven: bool
    specifications: dict[str, str] = Field(
        default_factory=dict,
        description="Free-form key-value specs like bandwidth, gain, noise_figure",
    )
    tags: list[str] = Field(
        default_factory=list,
        description="Additional freeform tags for search",
    )
    classified_by: ClassifiedBy
    classified_at: datetime
    local_path: str | None = Field(
        default=None,
        description="Relative path in repo if design is locally cloned",
    )
    readme_excerpt: str = Field(
        default="",
        description="First ~500 chars of README for display",
    )


class DesignDatabase(BaseModel):
    version: str = "1.0.0"
    generated_at: datetime
    designs: list[Design] = Field(default_factory=list)

    def find_by_id(self, design_id: str) -> Design | None:
        return next((d for d in self.designs if d.id == design_id), None)

    def find_by_source_url(self, url: str) -> Design | None:
        return next((d for d in self.designs if d.source_url == url), None)

    def filter_designs(
        self,
        *,
        pdk: PDK | None = None,
        circuit_class: CircuitClass | None = None,
        circuit_type: str | None = None,
        silicon_proven: bool | None = None,
    ) -> list[Design]:
        results = self.designs
        if pdk is not None:
            results = [d for d in results if d.pdk == pdk]
        if circuit_class is not None:
            results = [d for d in results if d.circuit_class == circuit_class]
        if circuit_type is not None:
            results = [
                d for d in results if circuit_type.lower() in [t.lower() for t in d.circuit_type]
            ]
        if silicon_proven is not None:
            results = [d for d in results if d.silicon_proven == silicon_proven]
        return results
