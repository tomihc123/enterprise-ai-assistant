import pytest

from app.infrastructure.document_processing.txt_document_extractor import (
    TxtDocumentExtractor,
)


def test_extracts_utf8_text():
    extractor = TxtDocumentExtractor()

    content = "Hello world".encode("utf-8")

    result = extractor.extract(content)

    assert result == "Hello world"


def test_extracts_unicode_text():
    extractor = TxtDocumentExtractor()

    content = "Hola España 日本語".encode("utf-8")

    result = extractor.extract(content)

    assert result == "Hola España 日本語"


def test_extracts_empty_file():
    extractor = TxtDocumentExtractor()

    result = extractor.extract(b"")

    assert result == ""


def test_rejects_invalid_utf8():
    extractor = TxtDocumentExtractor()

    invalid_content = b"\xff\xfe\xfa"

    with pytest.raises(UnicodeDecodeError):
        extractor.extract(invalid_content)