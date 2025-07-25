from fastapi import Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import daily_condition_router


@daily_condition_router.patch("/{daily_condition_id}")
async def update_daily_condition(
    daily_condition_id: UUID4,
    input: dto.UpdateDailyConditionInput,
    session: AsyncSession = Depends(get_session),
) -> dto.UpdateDailyConditionOutput:
    result = await usecase.update_daily_condition(session, daily_condition_id, input)
    if not result:
        raise HTTPException(status_code=404, detail="Daily condition not found")
    return result
