from core.models import es_helper


async def search_documents_ids(query_str: str) -> list[int]:
    response = await es_helper.client.search(
        index="documents",
        query={
            "match": {
                "text": query_str
            }
        },
        size=100
    )
    doc_ids = [int(hit["_id"]) for hit in response["hits"]["hits"]]
    return doc_ids