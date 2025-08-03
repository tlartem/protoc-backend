from fastapi import Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import group_router


@group_router.get("/{group_id}")
async def get_group(group_id: UUID4, session: AsyncSession = Depends(get_session)) -> dto.GetGroupOutput:
    try:
        return await usecase.get_group(session, group_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
