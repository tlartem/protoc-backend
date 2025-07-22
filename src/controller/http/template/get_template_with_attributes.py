from fastapi import Depends
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import template_router


@template_router.get("/{template_id}/with-attributes")
async def get_template_with_attributes(
    template_id: UUID4,
    session: AsyncSession = Depends(get_session),
) -> dto.GetTemplateWithAttributesOutput:
    return await usecase.get_template_with_attributes(session, template_id)
