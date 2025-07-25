from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import template_router


@template_router.post("/")
async def create_template(
    input: dto.CreateTemplateInput, session: AsyncSession = Depends(get_session)
) -> dto.CreateTemplateOutput:
    try:
        return await usecase.create_template(session, input)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
