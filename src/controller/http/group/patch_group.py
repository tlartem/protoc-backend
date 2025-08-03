from fastapi import Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import group_router


@group_router.patch("/{group_id}")
async def patch_group(
    group_id: UUID4,
    input: dto.PatchGroupInput,
    session: AsyncSession = Depends(get_session),
) -> dto.PatchGroupOutput:
    try:
        result = await usecase.patch_group(session, group_id, input)
        if not result:
            raise HTTPException(status_code=404, detail="Group not found")
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
