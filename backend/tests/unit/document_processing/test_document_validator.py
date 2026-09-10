import pytest

from app.infrastructure.document_processing.document_validator import (
    DocumentValidator,
)


def test_accepts_txt_file():
    validator = DocumentValidator()

    result = validator.validate_filename("document.txt")

    assert result == "document.txt"


def test_accepts_pdf_file():
    validator = DocumentValidator()

    result = validator.validate_filename("document.pdf")

    assert result == "document.pdf"


def test_accepts_uppercase_extension():
    validator = DocumentValidator()

    result = validator.validate_filename("document.PDF")

    assert result == "document.PDF"


def test_rejects_unsupported_extension():
    validator = DocumentValidator()

    with pytest.raises(
        ValueError,
        match="Unsupported file type: .jpg",
    ):
        validator.validate_filename("image.jpg")


def test_rejects_missing_filename():
    validator = DocumentValidator()

    with pytest.raises(
        ValueError,
        match="File must have a filename",
    ):
        validator.validate_filename(None)


def test_rejects_empty_filename():
    validator = DocumentValidator()

    with pytest.raises(
        ValueError,
        match="File must have a filename",
    ):
        validator.validate_filename("")


def test_accepts_file_with_valid_size():
    validator = DocumentValidator()

    content = b"a" * (5 * 1024 * 1024)

    validator.validate_size(content)


def test_rejects_file_larger_than_maximum_size():
    validator = DocumentValidator()

    content = b"a" * (5 * 1024 * 1024 + 1)

    with pytest.raises(
        ValueError,
        match="File exceeds maximum size of 5 MB",
    ):
        validator.validate_size(content)