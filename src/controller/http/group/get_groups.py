from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import group_router


@group_router.get("/")
async def get_groups(session: AsyncSession = Depends(get_session)) -> dto.GetGroupsOutput:
    try:
        return await usecase.get_groups(session)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
