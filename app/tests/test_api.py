import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_search_documents_success(client: AsyncClient, monkeypatch):
    async def mock_search_ids(query_str: str):
        return [1, 2]

    monkeypatch.setattr("api.search.search_documents_ids", mock_search_ids)

    response = await client.get("/api_v1/search", params={"query": "тест"})

    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_search_documents_empty(client: AsyncClient, monkeypatch):
    async def mock_search_ids(query_str: str):
        return []

    monkeypatch.setattr("api.search.search_documents_ids", mock_search_ids)

    response = await client.get("/api_v1/search", params={"query": "несуществующийзапрос"})

    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.asyncio
async def test_upload_csv_success(client: AsyncClient, monkeypatch):
    async def mock_csv_upload(file_bytes: bytes):
        pass

    monkeypatch.setattr("api.upload.csv_upload", mock_csv_upload)

    files = {"file": ("test.csv", b"text,created_date,rubrics\nhello,2019-01-01 00:00:00,['1']", "text/csv")}
    response = await client.post("/api_v1/upload_csv", files=files)

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "message": "CSV upload started in background",
    }


@pytest.mark.asyncio
async def test_remove_document_not_found(client: AsyncClient, monkeypatch):
    async def mock_delete_doc(id: int, session):
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Document not found")

    monkeypatch.setattr("api.documents.delete_doc", mock_delete_doc)

    response = await client.delete("/api_v1/documents/99999")

    assert response.status_code == 404