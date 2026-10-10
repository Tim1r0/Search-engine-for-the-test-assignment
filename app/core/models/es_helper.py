from elasticsearch import AsyncElasticsearch
from core.config import settings


class ElasticsearchHelper:
    def __init__(self, url: str):
        self.client = AsyncElasticsearch(url)

    async def close(self):
        await self.client.close()

es_helper = ElasticsearchHelper(str(settings.es.url))
