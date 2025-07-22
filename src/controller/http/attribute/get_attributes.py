from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import attribute_router


@attribute_router.get("/")
async def get_attributes(
    session: AsyncSession = Depends(get_session),
) -> dto.GetAttributesOutput:
    return await usecase.get_attributes(session)
