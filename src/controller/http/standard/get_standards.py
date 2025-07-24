from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import standard_router


@standard_router.get("/")
async def get_standards(
    session: AsyncSession = Depends(get_session),
) -> dto.GetStandardsOutput:
    return await usecase.get_standards(session)
