from fastapi import Depends
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import laboratory_router


@laboratory_router.get("/{laboratory_id}")
async def get_laboratory(
    laboratory_id: UUID4,
    session: AsyncSession = Depends(get_session),
) -> dto.GetLaboratoryOutput:
    return await usecase.get_laboratory(session, laboratory_id)
