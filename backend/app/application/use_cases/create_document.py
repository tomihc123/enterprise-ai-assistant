from app.domain.entities.document import Document
from app.domain.repositories.document_repository import DocumentRepository


class CreateDocumentUseCase:

    def __init__(self, repository: DocumentRepository):
        self.repository = repository

    def execute(
        self,
        name: str,
        content: str,
    ) -> Document:

        document = Document(
            id=None,
            name=name,
            content=content,
        )

        return self.repository.create(document)