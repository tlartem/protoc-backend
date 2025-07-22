from typing import Optional

from fastapi import APIRouter, Depends, Query
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

file_router = APIRouter(prefix="/files")


@file_router.get("/{file_id}")
async def get_file(
    file_id: UUID4,
    session: AsyncSession = Depends(get_session),
) -> dto.GetFileOutput:
    return await usecase.get_file(session, file_id)


@file_router.get("/")
async def get_files(
    template_id: Optional[UUID4] = Query(None, description="Фильтр по template_id"),
    session: AsyncSession = Depends(get_session),
) -> dto.GetFilesOutput:
    return await usecase.get_files(session, template_id)
