from app.domain.entities.document_chunk import DocumentChunk
from app.infrastructure.database.models.document_chunk_model import (
    DocumentChunkModel,
)


class DocumentChunkMapper:

    @staticmethod
    def to_model(
        entity: DocumentChunk,
    ) -> DocumentChunkModel:
        return DocumentChunkModel(
            document_id=entity.document_id,
            content=entity.content,
            chunk_index=entity.chunk_index,
        )

    @staticmethod
    def to_entity(
        model: DocumentChunkModel,
    ) -> DocumentChunk:
        return DocumentChunk(
            content=model.content,
            chunk_index=model.chunk_index,
            document_id=model.document_id,
        )

    @staticmethod
    def to_models(
        entities: list[DocumentChunk],
    ) -> list[DocumentChunkModel]:
        return [
            DocumentChunkMapper.to_model(entity)
            for entity in entities
        ]

    @staticmethod
    def to_entities(
        models: list[DocumentChunkModel],
    ) -> list[DocumentChunk]:
        return [
            DocumentChunkMapper.to_entity(model)
            for model in models
        ]