from fastapi import Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import template_router


@template_router.patch("/{template_id}")
async def patch_template(
    template_id: UUID4,
    input: dto.PatchTemplateInput,
    session: AsyncSession = Depends(get_session),
) -> dto.PatchTemplateOutput:
    result = await usecase.patch_template(session, template_id, input)
    if not result:
        raise HTTPException(status_code=404, detail="Template not found")
    return result
