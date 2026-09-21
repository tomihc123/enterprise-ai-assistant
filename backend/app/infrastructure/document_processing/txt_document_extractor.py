from app.infrastructure.document_processing.document_extractor import (
    DocumentExtractor,
)


class TxtDocumentExtractor(DocumentExtractor):

    def extract(self, content: bytes) -> str:
        return content.decode("utf-8")