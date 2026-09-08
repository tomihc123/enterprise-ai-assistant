from sqlalchemy.orm import Session

from app.domain.entities.document import Document
from app.domain.repositories.document_repository import DocumentRepository
from app.infrastructure.database.models.document_model import DocumentModel
from sqlalchemy import select


class DocumentRepositoryImpl(DocumentRepository):

    def __init__(self, db: Session):
        self.db = db

    def create(self, document: Document) -> Document:
        model = DocumentModel(
            name=document.name,
            content=document.content,
        )

        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)

        return Document(
            id=model.id,
            name=model.name,
            content=model.content,
            created_at=model.created_at,
        )

    def find_all(self) -> list[Document]:
        statement = select(DocumentModel)

        models = self.db.scalars(statement).all()

        return [
            Document(
                id=model.id,
                name=model.name,
                content=model.content,
                created_at=model.created_at,
            )
            for model in models
        ]      