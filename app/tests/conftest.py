import pytest
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import AsyncSession

from main import app
from core.models import db_helper


@pytest.fixture(scope="function")
async def db_session():
    async with db_helper.engine.connect() as connection:
        async with connection.begin() as trans:
            session = AsyncSession(
                bind=connection,
                expire_on_commit=False,
                join_transaction_mode="create_savepoint",
            )
            async def override_get_session():
                yield session

            app.dependency_overrides[db_helper.session_getter] = override_get_session

            yield session

            app.dependency_overrides.clear()
            await trans.rollback()


@pytest.fixture(scope="function")
async def client(db_session):
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac