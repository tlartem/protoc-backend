from fastapi import Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import template_router


@template_router.get("/{template_id}/attributes")
async def get_template_attributes(
    template_id: UUID4,
    session: AsyncSession = Depends(get_session),
) -> dto.GetTemplateAttributesOutput:
    result = await usecase.get_template_attributes(session, template_id)
    if not result:
        raise HTTPException(status_code=404, detail="Template not found")
    return result
