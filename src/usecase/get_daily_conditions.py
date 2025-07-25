import uuid
from datetime import date
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def get_daily_conditions(
    session: AsyncSession,
    laboratory_id: Optional[uuid.UUID] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
) -> dto.GetDailyConditionsOutput:
    if laboratory_id or start_date or end_date:
        daily_conditions = await postgres.daily_condition.get_by_date_range(
            session, laboratory_id, start_date, end_date
        )
    else:
        daily_conditions = await postgres.daily_condition.get_all(session)

    return dto.GetDailyConditionsOutput(daily_conditions=daily_conditions)
