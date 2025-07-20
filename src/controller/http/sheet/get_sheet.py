from fastapi import Depends
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import sheet_router


@sheet_router.get("/{sheet_id}")
async def get_sheet(
    sheet_id: UUID4,
    session: AsyncSession = Depends(get_session),
) -> dto.GetSheetOutput:
    return await usecase.get_sheet(session, sheet_id)
