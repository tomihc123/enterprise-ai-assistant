from fastapi import FastAPI

from app.api.routes.database import router as database_router
from app.api.routes.health import router as health_router
from app.api.routes.documents import router as documents_router
from app.core.config import settings


app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
)

app.include_router(health_router)
app.include_router(database_router)
app.include_router(documents_router)