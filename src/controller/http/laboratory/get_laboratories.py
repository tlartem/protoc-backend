from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import laboratory_router


@laboratory_router.get("/")
async def get_laboratories(
    session: AsyncSession = Depends(get_session),
) -> dto.GetLaboratoriesOutput:
    return await usecase.get_laboratories(session)
