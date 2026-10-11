from fastapi import APIRouter
from core.config import settings
from .upload import router as upload_router

router = APIRouter(
    prefix=settings.api_v1.api_pref
)

router.include_router(upload_router, tags=["upload_csv"])