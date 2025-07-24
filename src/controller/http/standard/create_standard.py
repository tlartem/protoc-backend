from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import standard_router


@standard_router.post("/")
async def create_standard(
    input: dto.CreateStandardInput, session: AsyncSession = Depends(get_session)
) -> dto.CreateStandardOutput:
    try:
        return await usecase.create_standard(session, input)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
