from fastapi import Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import group_router


@group_router.delete("/{group_id}")
async def delete_group(group_id: UUID4, session: AsyncSession = Depends(get_session)) -> dto.DeleteGroupOutput:
    try:
        return await usecase.delete_group(session, group_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
