import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from elasticsearch.exceptions import BadRequestError
from core.config import settings
from api import router as api_router
from core.models import db_helper, es_helper
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await es_helper.client.indices.create(
            index="documents",
            body={
                "mappings": {
                    "properties": {
                        "text": {"type": "text"}
                    }
                }
            }
        )
    except BadRequestError as e:
        if "resource_already_exists_exception" not in str(e):
            raise e
    yield
    await db_helper.dispose()
    await es_helper.close()


app = FastAPI(
    lifespan=lifespan,
)

app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run(
        app,
        host=settings.run.host,
        port=settings.run.port,
    )