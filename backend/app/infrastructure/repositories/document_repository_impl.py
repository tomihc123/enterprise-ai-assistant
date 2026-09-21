from sqlalchemy import select
from sqlalchemy.orm import Session

from app.domain.entities.document import Document
from app.domain.repositories.document_repository import DocumentRepository
from app.infrastructure.database.models.document_model import DocumentModel
from app.infrastructure.mappers.document_mapper import DocumentMapper


class DocumentRepositoryImpl(DocumentRepository):

    def __init__(self, db: Session):
        self.db = db

    def create(self, document: Document) -> Document:
        model = DocumentMapper.to_model(document)

        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)

        return DocumentMapper.to_domain(model)

    def find_all(self) -> list[Document]:
        statement = select(DocumentModel)
        models = self.db.scalars(statement).all()

        return [
            DocumentMapper.to_domain(model)
            for model in models
        ]