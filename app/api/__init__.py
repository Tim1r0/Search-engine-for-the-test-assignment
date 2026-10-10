from fastapi import APIRouter
from core.config import settings
router = APIRouter(
    prefix=settings.api_v1.api_pref
)