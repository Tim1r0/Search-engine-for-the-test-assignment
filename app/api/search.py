from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from crud.get_doc import get_sorted_documents_by_ids
from services.search_service import search_documents_ids
from core import settings
from core.models import db_helper
from core.schemas import SearchResponse

router = APIRouter(
    prefix=settings.api_v1.search
)

@router.get('', response_model=list[SearchResponse])
async def api_search_documents(
    query: str,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter)
    ]
):
    doc_ids = await search_documents_ids(query)
    if not doc_ids:
        return []
    documents = await get_sorted_documents_by_ids(session, doc_ids)
    return documents
