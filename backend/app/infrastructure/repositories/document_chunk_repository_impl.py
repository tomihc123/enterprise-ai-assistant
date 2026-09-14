from sqlalchemy import select
from sqlalchemy.orm import Session

from app.domain.entities.document_chunk import DocumentChunk
from app.domain.repositories.document_chunk_repository import (
    DocumentChunkRepository,
)
from app.infrastructure.database.models.document_chunk_model import (
    DocumentChunkModel,
)
from app.infrastructure.mappers.document_chunk_mapper import (
    DocumentChunkMapper,
)


class DocumentChunkRepositoryImpl(DocumentChunkRepository):

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def save_all(
        self,
        chunks: list[DocumentChunk],
    ) -> list[DocumentChunk]:

        models = DocumentChunkMapper.to_models(chunks)

        self.db.add_all(models)
        self.db.commit()

        for model in models:
            self.db.refresh(model)

        return DocumentChunkMapper.to_entities(models)

    def find_by_document_id(
        self,
        document_id: int,
    ) -> list[DocumentChunk]:

        statement = (
            select(DocumentChunkModel)
            .where(
                DocumentChunkModel.document_id == document_id
            )
            .order_by(
                DocumentChunkModel.chunk_index
            )
        )

        models = list(
            self.db.scalars(statement).all()
        )

        return DocumentChunkMapper.to_entities(models)