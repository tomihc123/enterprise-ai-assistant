from app.application.services.embedding_service import EmbeddingService
from app.domain.entities.document_chunk import DocumentChunk


class GenerateChunkEmbeddings:

    def __init__(
        self,
        embedding_service: EmbeddingService,
    ):
        self.embedding_service = embedding_service

    def execute(
        self,
        chunks: list[DocumentChunk],
    ) -> list[DocumentChunk]:

        if not chunks:
            return []

        texts = [
            chunk.content
            for chunk in chunks
        ]

        embeddings = self.embedding_service.embed_texts(
            texts
        )

        if len(embeddings) != len(chunks):
            raise ValueError(
                "Embedding service returned an unexpected "
                "number of embeddings"
            )

        for chunk, embedding in zip(
            chunks,
            embeddings,
            strict=True,
        ):
            chunk.embedding = embedding

        return chunks