from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from crud.del_doc import delete_doc

router = APIRouter(
    prefix="/documents"
)



@router.delete("/{document_id}", status_code=status.HTTP_200_OK)
async def remove_document(
    document_id: int,
    session: AsyncSession = Depends(db_helper.session_getter)
):
    return await delete_doc(id=document_id, session=session)