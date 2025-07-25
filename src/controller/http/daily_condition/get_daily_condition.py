from fastapi import Depends
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import daily_condition_router


@daily_condition_router.get("/{daily_condition_id}")
async def get_daily_condition(
    daily_condition_id: UUID4,
    session: AsyncSession = Depends(get_session),
) -> dto.GetDailyConditionOutput:
    return await usecase.get_daily_condition(session, daily_condition_id)
