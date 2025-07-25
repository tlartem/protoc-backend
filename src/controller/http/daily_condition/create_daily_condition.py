from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import daily_condition_router


@daily_condition_router.post("/")
async def create_daily_condition(
    input: dto.CreateDailyConditionInput, session: AsyncSession = Depends(get_session)
) -> dto.CreateDailyConditionOutput:
    try:
        return await usecase.create_daily_condition(session, input)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
