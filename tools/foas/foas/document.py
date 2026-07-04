from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class FoasDocument:
    path: Path
    id: str | None
    title: str | None
    status: str | None
    version: str | None
    owner: str | None
    depends_on: list[str] = field(default_factory=list)
    references: list[str] = field(default_factory=list)
    implemented_by: list[str] = field(default_factory=list)
    raw_front_matter: dict = field(default_factory=dict)
