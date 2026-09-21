from dataclasses import dataclass


@dataclass
class DocumentChunk:
    content: str
    chunk_index: int
    document_id: int | None = None
    embedding: list[float] | None = None