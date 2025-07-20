from fastapi import Depends
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import template_router


@template_router.get("/{template_id}")
async def get_template(
    template_id: UUID4,
    session: AsyncSession = Depends(get_session),
) -> dto.GetTemplateOutput:
    return await usecase.get_template(session, template_id)
