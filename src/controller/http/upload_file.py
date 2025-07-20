import fastapi
from fastapi import APIRouter, Depends, UploadFile
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

upload_file_router = APIRouter(prefix="/files")


@upload_file_router.post("/upload")
async def upload_file(
    file: UploadFile = fastapi.File(...),
    template_id: UUID4 = fastapi.Query(...),
    session: AsyncSession = Depends(get_session),
) -> dto.UploadFileOutput:
    return await usecase.upload_file(session, file, template_id)
