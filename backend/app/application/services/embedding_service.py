from abc import ABC, abstractmethod


class EmbeddingService(ABC):

    @abstractmethod
    def embed_text(
        self,
        text: str,
    ) -> list[float]:
        pass

    @abstractmethod
    def embed_texts(
        self,
        texts: list[str],
    ) -> list[list[float]]:
        pass