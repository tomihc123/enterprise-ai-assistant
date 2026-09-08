from pathlib import Path

from app.infrastructure.document_processing.document_extractor import (
    DocumentExtractor,
)
from app.infrastructure.document_processing.pdf_document_extractor import (
    PdfDocumentExtractor,
)
from app.infrastructure.document_processing.txt_document_extractor import (
    TxtDocumentExtractor,
)


class DocumentExtractorFactory:

    _extractors: dict[str, type[DocumentExtractor]] = {
        ".txt": TxtDocumentExtractor,
        ".pdf": PdfDocumentExtractor,
    }

    @classmethod
    def create(cls, filename: str) -> DocumentExtractor:
        extension = Path(filename).suffix.lower()

        extractor_class = cls._extractors.get(extension)

        if extractor_class is None:
            raise ValueError(
                f"No extractor available for file type: {extension}"
            )

        return extractor_class()