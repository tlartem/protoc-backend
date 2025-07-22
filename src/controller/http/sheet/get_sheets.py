from typing import Optional

from fastapi import Depends, Query
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import sheet_router


@sheet_router.get("/")
async def get_sheets(
    template_id: Optional[UUID4] = Query(None, description="Фильтр по template_id"),
    session: AsyncSession = Depends(get_session),
) -> dto.GetSheetsOutput:
    return await usecase.get_sheets(session, template_id)
