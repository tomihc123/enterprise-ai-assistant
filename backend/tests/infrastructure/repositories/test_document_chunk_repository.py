from sqlalchemy.orm import Session

from app.domain.entities.document_chunk import DocumentChunk
from app.infrastructure.database.models.document_model import DocumentModel
from app.infrastructure.database.session import SessionLocal
from app.infrastructure.repositories.document_chunk_repository_impl import (
    DocumentChunkRepositoryImpl,
)


def test_save_and_find_document_chunks():
    db: Session = SessionLocal()

    try:
        document = DocumentModel(
            name="test_document.txt",
            content="Test document content",
        )

        db.add(document)
        db.commit()
        db.refresh(document)

        repository = DocumentChunkRepositoryImpl(db)

        chunks = [
            DocumentChunk(
                content="This is the first chunk.",
                chunk_index=0,
                document_id=document.id,
            ),
            DocumentChunk(
                content="This is the second chunk.",
                chunk_index=1,
                document_id=document.id,
            ),
            DocumentChunk(
                content="This is the third chunk.",
                chunk_index=2,
                document_id=document.id,
            ),
        ]

        saved_chunks = repository.save_all(chunks)

        assert len(saved_chunks) == 3

        found_chunks = repository.find_by_document_id(
            document.id
        )

        assert len(found_chunks) == 3

        assert found_chunks[0].content == "This is the first chunk."
        assert found_chunks[1].content == "This is the second chunk."
        assert found_chunks[2].content == "This is the third chunk."

        assert found_chunks[0].chunk_index == 0
        assert found_chunks[1].chunk_index == 1
        assert found_chunks[2].chunk_index == 2

        assert found_chunks[0].document_id == document.id
        assert found_chunks[1].document_id == document.id
        assert found_chunks[2].document_id == document.id

    finally:
        db.query(DocumentModel).filter(
            DocumentModel.name == "test_document.txt"
        ).delete()

        db.commit()
        db.close()