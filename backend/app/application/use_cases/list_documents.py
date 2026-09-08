from app.domain.entities.document import Document
from app.domain.repositories.document_repository import DocumentRepository


class ListDocumentsUseCase:

    def __init__(self, repository: DocumentRepository):
        self.repository = repository

    def execute(self) -> list[Document]:
        return self.repository.find_all()