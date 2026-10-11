from fastapi import APIRouter
from core.config import settings
from .upload import router as upload_router
from .search import router as search_router
from .documents import router as document_router
router = APIRouter(
    prefix=settings.api_v1.api_pref
)

router.include_router(upload_router, tags=["upload_csv"])
router.include_router(search_router, tags=["search"])
router.include_router(document_router, tags=["documents"])