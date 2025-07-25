import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def get_daily_condition(
    session: AsyncSession, daily_condition_id: uuid.UUID
) -> dto.GetDailyConditionOutput:
    daily_condition = await postgres.daily_condition.get(session, daily_condition_id)
    return dto.GetDailyConditionOutput(daily_condition=daily_condition)
