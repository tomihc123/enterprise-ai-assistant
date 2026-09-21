from sentence_transformers import SentenceTransformer

from app.application.services.embedding_service import EmbeddingService


DEFAULT_EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
EMBEDDING_DIMENSION = 384


class SentenceTransformerEmbeddingService(EmbeddingService):

    def __init__(
        self,
        model_name: str = DEFAULT_EMBEDDING_MODEL,
    ):
        self.model = SentenceTransformer(model_name)

    def embed_text(
        self,
        text: str,
    ) -> list[float]:

        if not text.strip():
            raise ValueError(
                "Text cannot be empty when generating an embedding"
            )

        embedding = self.model.encode(
            text,
            normalize_embeddings=True,
        )

        return embedding.tolist()

    def embed_texts(
        self,
        texts: list[str],
    ) -> list[list[float]]:

        if not texts:
            return []

        if any(
            not text.strip()
            for text in texts
        ):
            raise ValueError(
                "Texts cannot contain empty values"
            )

        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True,
        )

        return embeddings.tolist()