from datetime import datetime

from pydantic import BaseModel


class CreateDocumentRequest(BaseModel):
    name: str
    content: str


class DocumentResponse(BaseModel):
    id: int
    name: str
    content: str
    created_at: datetime