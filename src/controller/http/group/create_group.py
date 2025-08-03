from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import group_router


@group_router.post("/")
async def create_group(
    input: dto.CreateGroupInput, session: AsyncSession = Depends(get_session)
) -> dto.CreateGroupOutput:
    try:
        return await usecase.create_group(session, input)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
