import pytest

from app.infrastructure.document_processing.document_extractor_factory import (
    DocumentExtractorFactory,
)
from app.infrastructure.document_processing.pdf_document_extractor import (
    PdfDocumentExtractor,
)
from app.infrastructure.document_processing.txt_document_extractor import (
    TxtDocumentExtractor,
)


def test_returns_txt_document_extractor():
    extractor = DocumentExtractorFactory.create(
        "document.txt"
    )

    assert isinstance(
        extractor,
        TxtDocumentExtractor,
    )


def test_returns_pdf_document_extractor():
    extractor = DocumentExtractorFactory.create(
        "document.pdf"
    )

    assert isinstance(
        extractor,
        PdfDocumentExtractor,
    )


def test_extension_is_case_insensitive():
    extractor = DocumentExtractorFactory.create(
        "document.PDF"
    )

    assert isinstance(
        extractor,
        PdfDocumentExtractor,
    )


def test_rejects_unknown_extension():
    with pytest.raises(
        ValueError,
        match="No extractor available for file type: .docx",
    ):
        DocumentExtractorFactory.create(
            "document.docx"
        )