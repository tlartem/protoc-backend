from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import attribute_router


@attribute_router.post("/")
async def create_attribute(
    input: dto.CreateAttributeInput, session: AsyncSession = Depends(get_session)
) -> dto.CreateAttributeOutput:
    try:
        return await usecase.create_attribute(session, input)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
