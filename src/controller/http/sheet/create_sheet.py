from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import sheet_router


@sheet_router.post("/")
async def create_sheet(
    input: dto.CreateSheetInput, session: AsyncSession = Depends(get_session)
) -> dto.CreateSheetOutput:
    return await usecase.create_sheet(session, input)
