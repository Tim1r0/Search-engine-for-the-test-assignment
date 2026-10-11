from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Document


async def get_sorted_documents_by_ids(
    session: AsyncSession,
    doc_ids: list[int],
):
    if not doc_ids:
        return []
    stmt = (
        select(Document)
        .where(Document.id.in_(doc_ids))
        .order_by(Document.created_date.desc())
        .limit(20)
    )
    result = await session.scalars(stmt)
    return result.all()