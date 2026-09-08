from pathlib import Path


class DocumentValidator:

    ALLOWED_EXTENSIONS = {
        ".txt",
        ".pdf",
    }

    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

    def validate_filename(self, filename: str | None) -> str:
        if not filename:
            raise ValueError("File must have a filename")

        extension = Path(filename).suffix.lower()

        if extension not in self.ALLOWED_EXTENSIONS:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )

        return filename

    def validate_size(self, content: bytes) -> None:
        if len(content) > self.MAX_FILE_SIZE:
            raise ValueError(
                "File exceeds maximum size of 5 MB"
            )