from fastapi import Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import template_router


@template_router.post("/{template_id}/attributes")
async def set_template_attributes(
    template_id: UUID4,
    input: dto.SetTemplateAttributesInput,
    session: AsyncSession = Depends(get_session),
) -> list[dto.SetTemplateAttributeOutput]:
    try:
        return await usecase.set_template_attributes(session, template_id, input)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
