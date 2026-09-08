from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError

from app.api.exceptions.handlers import (
    http_exception_handler,
    validation_exception_handler,
)
from app.api.routes.database import router as database_router
from app.api.routes.documents import router as documents_router
from app.api.routes.health import router as health_router
from app.core.config import settings


app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
)


app.add_exception_handler(
    HTTPException,
    http_exception_handler,
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler,
)


app.include_router(health_router)
app.include_router(database_router)
app.include_router(documents_router)