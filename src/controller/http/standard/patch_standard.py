from fastapi import Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import standard_router


@standard_router.patch("/{standard_id}")
async def patch_standard(
    standard_id: UUID4,
    input: dto.PatchStandardInput,
    session: AsyncSession = Depends(get_session),
) -> dto.PatchStandardOutput:
    result = await usecase.patch_standard(session, standard_id, input)
    if not result:
        raise HTTPException(status_code=404, detail="Standard not found")
    return result
