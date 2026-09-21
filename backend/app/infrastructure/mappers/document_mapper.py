from app.domain.entities.document import Document
from app.infrastructure.database.models.document_model import DocumentModel


class DocumentMapper:

    @staticmethod
    def to_model(document: Document) -> DocumentModel:
        return DocumentModel(
            name=document.name,
            content=document.content,
        )

    @staticmethod
    def to_domain(model: DocumentModel) -> Document:
        return Document(
            id=model.id,
            name=model.name,
            content=model.content,
            created_at=model.created_at,
        )