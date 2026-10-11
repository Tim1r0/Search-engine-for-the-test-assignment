from fastapi import APIRouter, UploadFile, File, BackgroundTasks, HTTPException, status
from services.process_csv_upload import csv_upload
from core.config import settings

router = APIRouter(
    prefix=settings.api_v1.upload_csv
)

@router.post('')
async def upload_csv_endpoint(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
):
    file_bytes = await file.read()
    if file_bytes is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    background_tasks.add_task(csv_upload, file_bytes)

    return {
        'status': 'ok',
        'message': 'CSV upload started in background',
    }
