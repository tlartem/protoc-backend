from fastapi import Depends
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import standard_router


@standard_router.get("/{standard_id}")
async def get_standard(
    standard_id: UUID4,
    session: AsyncSession = Depends(get_session),
) -> dto.GetStandardOutput:
    return await usecase.get_standard(session, standard_id)
