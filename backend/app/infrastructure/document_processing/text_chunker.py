from app.domain.entities.document_chunk import DocumentChunk


class TextChunker:

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        if chunk_overlap >= chunk_size:
            raise ValueError(
                "chunk_overlap must be smaller than chunk_size"
            )

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split(
        self,
        text: str,
        document_id: int | None = None,
    ) -> list[DocumentChunk]:

        text = self._normalize_text(text)

        if not text:
            return []

        chunks: list[DocumentChunk] = []

        start = 0
        chunk_index = 0

        while start < len(text):

            end = min(
                start + self.chunk_size,
                len(text),
            )

            if end < len(text):
                end = self._find_best_break_point(
                    text=text,
                    start=start,
                    end=end,
                )

            chunk_content = text[start:end].strip()

            if chunk_content:
                chunks.append(
                    DocumentChunk(
                        content=chunk_content,
                        chunk_index=chunk_index,
                        document_id=document_id,
                    )
                )

                chunk_index += 1

            if end >= len(text):
                break

            start = max(
                end - self.chunk_overlap,
                start + 1,
            )

        return chunks

    @staticmethod
    def _normalize_text(text: str) -> str:
        return " ".join(text.split())

    @staticmethod
    def _find_best_break_point(
        text: str,
        start: int,
        end: int,
    ) -> int:

        separators = [
            "\n\n",
            ". ",
            "! ",
            "? ",
            "; ",
            ", ",
            " ",
        ]

        for separator in separators:

            position = text.rfind(
                separator,
                start,
                end,
            )

            if position != -1:
                return position + len(separator)

        return end