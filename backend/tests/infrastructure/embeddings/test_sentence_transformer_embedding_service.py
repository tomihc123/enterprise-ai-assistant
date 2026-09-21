import pytest

from app.infrastructure.embeddings.sentence_transformer_embedding_service import (
    EMBEDDING_DIMENSION,
    SentenceTransformerEmbeddingService,
)


@pytest.fixture(scope="module")
def embedding_service() -> SentenceTransformerEmbeddingService:
    return SentenceTransformerEmbeddingService()


def test_embed_text_returns_expected_dimension(
    embedding_service: SentenceTransformerEmbeddingService,
):
    embedding = embedding_service.embed_text(
        "Employees can work remotely."
    )

    assert len(embedding) == EMBEDDING_DIMENSION
    assert all(
        isinstance(value, float)
        for value in embedding
    )


def test_embed_texts_returns_one_embedding_per_text(
    embedding_service: SentenceTransformerEmbeddingService,
):
    texts = [
        "FastAPI is used for the API.",
        "PostgreSQL stores application data.",
        "RAG retrieves relevant information.",
    ]

    embeddings = embedding_service.embed_texts(texts)

    assert len(embeddings) == len(texts)

    for embedding in embeddings:
        assert len(embedding) == EMBEDDING_DIMENSION


def test_embed_text_rejects_empty_text(
    embedding_service: SentenceTransformerEmbeddingService,
):
    with pytest.raises(
        ValueError,
        match="Text cannot be empty",
    ):
        embedding_service.embed_text("")


def test_embed_texts_returns_empty_list_for_empty_input(
    embedding_service: SentenceTransformerEmbeddingService,
):
    embeddings = embedding_service.embed_texts([])

    assert embeddings == []


def test_embed_texts_rejects_empty_values(
    embedding_service: SentenceTransformerEmbeddingService,
):
    with pytest.raises(
        ValueError,
        match="Texts cannot contain empty values",
    ):
        embedding_service.embed_texts(
            [
                "Valid text",
                "",
            ]
        )