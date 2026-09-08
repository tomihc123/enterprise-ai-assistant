from fastapi import APIRouter, Depends, File, UploadFile, status, HTTPException
from sqlalchemy.orm import Session

from app.api.schemas.document import (
    CreateDocumentRequest,
    DocumentResponse,
)
from app.api.schemas.response import ApiResponse
from app.application.use_cases.create_document import CreateDocumentUseCase
from app.application.use_cases.list_documents import ListDocumentsUseCase
from app.infrastructure.database.session import get_db
from app.infrastructure.repositories.document_repository_impl import (
    DocumentRepositoryImpl,
)
from app.infrastructure.document_processing.document_validator import (
    DocumentValidator,
)
from app.infrastructure.document_processing.document_extractor_factory import (
    DocumentExtractorFactory,
)


router = APIRouter(
    prefix="/documents",
    tags=["documents"],
)


@router.post(
    "",
    response_model=ApiResponse[DocumentResponse],
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

    data = DocumentResponse(
        id=document.id,
        name=document.name,
        content=document.content,
        created_at=document.created_at,
    )

    return ApiResponse(
        status=status.HTTP_201_CREATED,
        detail="Document created successfully",
        data=data,
    )


@router.get(
    "",
    response_model=ApiResponse[list[DocumentResponse]],
    status_code=status.HTTP_200_OK,
)
def list_documents(
    db: Session = Depends(get_db),
):
    repository = DocumentRepositoryImpl(db)
    use_case = ListDocumentsUseCase(repository)

    documents = use_case.execute()

    data = [
        DocumentResponse(
            id=document.id,
            name=document.name,
            content=document.content,
            created_at=document.created_at,
        )
        for document in documents
    ]

    return ApiResponse(
        status=status.HTTP_200_OK,
        detail="Documents retrieved successfully",
        data=data,
    )


@router.post(
    "/upload",
    response_model=ApiResponse[DocumentResponse],
    status_code=status.HTTP_201_CREATED,
)
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    validator = DocumentValidator()

    try:
        filename = validator.validate_filename(file.filename)

        content_bytes = await file.read()

        validator.validate_size(content_bytes)

        extractor = DocumentExtractorFactory.create(filename)
        content = extractor.extract(content_bytes)

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc

    repository = DocumentRepositoryImpl(db)
    use_case = CreateDocumentUseCase(repository)

    document = use_case.execute(
        name=filename,
        content=content,
    )

    data = DocumentResponse(
        id=document.id,
        name=document.name,
        content=document.content,
        created_at=document.created_at,
    )

    return ApiResponse(
        status=status.HTTP_201_CREATED,
        detail="Document uploaded successfully",
        data=data,
    )