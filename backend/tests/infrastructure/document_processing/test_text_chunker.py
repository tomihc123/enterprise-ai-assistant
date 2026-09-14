import pytest

from app.infrastructure.document_processing.text_chunker import TextChunker


def test_split_text_into_chunks():
    text = (
        "FastAPI is a modern Python framework. "
        "SQLAlchemy is an ORM for Python. "
        "PostgreSQL is a relational database."
    )

    chunker = TextChunker(
        chunk_size=50,
        chunk_overlap=10,
    )

    chunks = chunker.split(text)

    assert len(chunks) > 1
    assert chunks[0].chunk_index == 0
    assert chunks[1].chunk_index == 1
    assert chunks[0].content
    assert chunks[1].content


def test_empty_text_returns_empty_list():
    chunker = TextChunker()

    chunks = chunker.split("")

    assert chunks == []


def test_overlap_cannot_be_greater_than_chunk_size():
    with pytest.raises(ValueError):
        TextChunker(
            chunk_size=100,
            chunk_overlap=100,
        )