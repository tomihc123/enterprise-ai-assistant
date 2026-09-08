from io import BytesIO

from pypdf import PdfReader

from app.infrastructure.document_processing.document_extractor import (
    DocumentExtractor,
)


class PdfDocumentExtractor(DocumentExtractor):

    def extract(self, content: bytes) -> str:
        reader = PdfReader(BytesIO(content))

        pages_text = []

        for page in reader.pages:
            text = page.extract_text()

            if text:
                pages_text.append(text)

        extracted_text = "\n".join(pages_text).strip()

        if not extracted_text:
            raise ValueError(
                "No extractable text found in PDF"
            )

        return extracted_text