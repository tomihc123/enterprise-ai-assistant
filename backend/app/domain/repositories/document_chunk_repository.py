from abc import ABC, abstractmethod

from app.domain.entities.document_chunk import DocumentChunk


class DocumentChunkRepository(ABC):

    @abstractmethod
    def save_all(
        self,
        chunks: list[DocumentChunk],
    ) -> list[DocumentChunk]:
        pass

    @abstractmethod
    def find_by_document_id(
        self,
        document_id: int,
    ) -> list[DocumentChunk]:
        pass