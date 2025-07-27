from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import template_router


@template_router.post("/copy", response_model=dto.CopyTemplateOutput)
async def copy_template(
    _input: dto.CopyTemplateInput,
    session: AsyncSession = Depends(get_session),
) -> dto.CopyTemplateOutput:
    """Копирует существующий шаблон со всеми связанными данными"""
    return await usecase.copy_template(_input, session)
