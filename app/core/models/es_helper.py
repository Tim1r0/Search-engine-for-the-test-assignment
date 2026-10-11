from elasticsearch import AsyncElasticsearch
from core.config import settings


class ElasticsearchHelper:
    def __init__(self, url: str):
        self.client = AsyncElasticsearch(
            url,
            headers={"Accept": "application/vnd.elasticsearch+json; compatible-with=8"}
        )

    async def close(self):
        await self.client.close()

es_helper = ElasticsearchHelper(str(settings.es.url))
