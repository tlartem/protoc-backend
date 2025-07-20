from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import sheet_router


@sheet_router.get("/")
async def get_sheets(
    session: AsyncSession = Depends(get_session),
) -> dto.GetSheetsOutput:
    return await usecase.get_sheets(session)
