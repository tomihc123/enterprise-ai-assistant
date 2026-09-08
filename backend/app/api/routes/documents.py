from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.schemas.document import (
    CreateDocumentRequest,
    DocumentResponse,
)
from app.application.use_cases.create_document import CreateDocumentUseCase
from app.application.use_cases.list_documents import ListDocumentsUseCase
from app.infrastructure.database.session import get_db
from app.infrastructure.repositories.document_repository_impl import (
    DocumentRepositoryImpl,
)


router = APIRouter(
    prefix="/documents",
    tags=["documents"],
)


@router.post(
    "",
    response_model=DocumentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_document(
    request: CreateDocumentRequest,
    db: Session = Depends(get_db),
):
    repository = DocumentRepositoryImpl(db)

    use_case = CreateDocumentUseCase(repository)

    document = use_case.execute(
        name=request.name,
        content=request.content,
    )

    return DocumentResponse(
        id=document.id,
        name=document.name,
        content=document.content,
        created_at=document.created_at,
    )

@router.get(
    "",
    response_model=list[DocumentResponse],
)
def list_documents(
    db: Session = Depends(get_db),
):
    repository = DocumentRepositoryImpl(db)

    use_case = ListDocumentsUseCase(repository)

    documents = use_case.execute()

    return [
        DocumentResponse(
            id=document.id,
            name=document.name,
            content=document.content,
            created_at=document.created_at,
        )
        for document in documents
    ]