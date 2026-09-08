from abc import ABC, abstractmethod

from app.domain.entities.document import Document


class DocumentRepository(ABC):

    @abstractmethod
    def create(self, document: Document) -> Document:
        pass

    @abstractmethod
    def find_all(self) -> list[Document]:
        pass       