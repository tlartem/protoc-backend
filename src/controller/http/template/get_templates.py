from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import template_router


@template_router.get("/")
async def get_templates(
    session: AsyncSession = Depends(get_session),
) -> dto.GetTemplatesOutput:
    return await usecase.get_templates(session)
