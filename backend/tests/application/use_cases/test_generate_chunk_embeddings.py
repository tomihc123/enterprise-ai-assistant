from app.application.services.embedding_service import EmbeddingService
from app.application.use_cases.generate_chunk_embeddings import (
    GenerateChunkEmbeddings,
)
from app.domain.entities.document_chunk import DocumentChunk


class FakeEmbeddingService(EmbeddingService):

    def embed_text(
        self,
        text: str,
    ) -> list[float]:
        return [0.1, 0.2, 0.3]

    def embed_texts(
        self,
        texts: list[str],
    ) -> list[list[float]]:
        return [
            [float(index), 0.1, 0.2]
            for index, _ in enumerate(texts)
        ]


def test_generate_embeddings_for_chunks():
    chunks = [
        DocumentChunk(
            content="Remote work policy",
            chunk_index=0,
            document_id=1,
        ),
        DocumentChunk(
            content="Annual leave policy",
            chunk_index=1,
            document_id=1,
        ),
    ]

    embedding_service = FakeEmbeddingService()

    use_case = GenerateChunkEmbeddings(
        embedding_service=embedding_service,
    )

    result = use_case.execute(chunks)

    assert len(result) == 2

    assert result[0].embedding == [
        0.0,
        0.1,
        0.2,
    ]

    assert result[1].embedding == [
        1.0,
        0.1,
        0.2,
    ]


def test_generate_embeddings_with_empty_chunks():
    embedding_service = FakeEmbeddingService()

    use_case = GenerateChunkEmbeddings(
        embedding_service=embedding_service,
    )

    result = use_case.execute([])

    assert result == []