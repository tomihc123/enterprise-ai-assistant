from sqlalchemy import delete
from sqlalchemy.orm import Session

from app.application.use_cases.generate_chunk_embeddings import (
    GenerateChunkEmbeddings,
)
from app.domain.entities.document_chunk import DocumentChunk
from app.infrastructure.database.models.document_model import DocumentModel
from app.infrastructure.database.session import SessionLocal
from app.infrastructure.embeddings.sentence_transformer_embedding_service import (
    EMBEDDING_DIMENSION,
    SentenceTransformerEmbeddingService,
)
from app.infrastructure.repositories.document_chunk_repository_impl import (
    DocumentChunkRepositoryImpl,
)


def test_save_and_retrieve_chunk_with_embedding():
    db: Session = SessionLocal()
    document_id: int | None = None

    try:
        document = DocumentModel(
            name="embedding_test.txt",
            content="Employees can work remotely three days per week.",
        )

        db.add(document)
        db.commit()
        db.refresh(document)

        document_id = document.id

        chunks = [
            DocumentChunk(
                content="Employees can work remotely three days per week.",
                chunk_index=0,
                document_id=document.id,
            )
        ]

        embedding_service = SentenceTransformerEmbeddingService()

        generate_embeddings = GenerateChunkEmbeddings(
            embedding_service=embedding_service,
        )

        chunks_with_embeddings = generate_embeddings.execute(
            chunks
        )

        assert chunks_with_embeddings[0].embedding is not None
        assert (
            len(chunks_with_embeddings[0].embedding)
            == EMBEDDING_DIMENSION
        )

        repository = DocumentChunkRepositoryImpl(db)

        repository.save_all(
            chunks_with_embeddings
        )

        stored_chunks = repository.find_by_document_id(
            document.id
        )

        assert len(stored_chunks) == 1

        stored_chunk = stored_chunks[0]

        assert stored_chunk.embedding is not None
        assert len(stored_chunk.embedding) == EMBEDDING_DIMENSION

        assert stored_chunk.content == (
            "Employees can work remotely three days per week."
        )

    finally:
        db.rollback()

        if document_id is not None:
            db.execute(
                delete(DocumentModel).where(
                    DocumentModel.id == document_id
                )
            )
            db.commit()

        db.close()