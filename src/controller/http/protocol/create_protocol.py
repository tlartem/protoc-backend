from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import protocol_router


@protocol_router.post("/")
async def create_protocol(
    input: dto.CreateProtocolInput, session: AsyncSession = Depends(get_session)
) -> dto.CreateProtocolOutput:
    return await usecase.create_protocol(session, input)
