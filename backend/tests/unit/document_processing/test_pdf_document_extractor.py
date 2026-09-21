import pytest

import app.infrastructure.document_processing.pdf_document_extractor as pdf_module

from app.infrastructure.document_processing.pdf_document_extractor import (
    PdfDocumentExtractor,
)


class FakePage:

    def __init__(self, text: str | None):
        self.text = text

    def extract_text(self):
        return self.text


def test_extracts_text_from_pdf(monkeypatch):

    class FakePdfReader:

        def __init__(self, content):
            self.pages = [
                FakePage("First page"),
                FakePage("Second page"),
            ]

    monkeypatch.setattr(
        pdf_module,
        "PdfReader",
        FakePdfReader,
    )

    extractor = PdfDocumentExtractor()

    result = extractor.extract(
        b"fake pdf bytes"
    )

    assert result == "First page\nSecond page"


def test_ignores_pages_without_text(monkeypatch):

    class FakePdfReader:

        def __init__(self, content):
            self.pages = [
                FakePage("First page"),
                FakePage(None),
                FakePage("Third page"),
            ]

    monkeypatch.setattr(
        pdf_module,
        "PdfReader",
        FakePdfReader,
    )

    extractor = PdfDocumentExtractor()

    result = extractor.extract(
        b"fake pdf bytes"
    )

    assert result == "First page\nThird page"


def test_rejects_pdf_without_extractable_text(
    monkeypatch,
):

    class FakePdfReader:

        def __init__(self, content):
            self.pages = [
                FakePage(None),
                FakePage(""),
            ]

    monkeypatch.setattr(
        pdf_module,
        "PdfReader",
        FakePdfReader,
    )

    extractor = PdfDocumentExtractor()

    with pytest.raises(
        ValueError,
        match="No extractable text found in PDF",
    ):
        extractor.extract(
            b"fake pdf bytes"
        )