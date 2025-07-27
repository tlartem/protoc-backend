import uuid

from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import template_router


@template_router.delete("/{template_id}", response_model=dto.DeleteTemplateOutput)
async def delete_template(
    template_id: uuid.UUID,
    session: AsyncSession = Depends(get_session),
) -> dto.DeleteTemplateOutput:
    """Удаляет шаблон по ID"""
    try:
        return await usecase.delete_template(template_id, session)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
