from dataclasses import dataclass
from datetime import datetime


@dataclass
class Document:
    id: int | None
    name: str
    content: str
    created_at: datetime | None = None