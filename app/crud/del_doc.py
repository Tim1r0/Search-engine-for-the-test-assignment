from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Document, es_helper
from elasticsearch import NotFoundError


async def delete_doc(
    id: int,
    session: AsyncSession,
):
    doc = await session.get(Document, id)
    if not doc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Document not found")
    await session.delete(doc)
    await session.commit()
    try:
        await es_helper.client.delete(
            index="documents",
            id=str(id)
        )
    except NotFoundError:
        pass
    return {"status": "ok", "message": f"Document {id} deleted successfully"}
