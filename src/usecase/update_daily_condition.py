import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def update_daily_condition(
    session: AsyncSession,
    daily_condition_id: uuid.UUID,
    _input: dto.UpdateDailyConditionInput,
) -> dto.UpdateDailyConditionOutput | None:
    update_data = {}
    if _input.laboratory_id is not None:
        update_data["laboratory_id"] = _input.laboratory_id
    if _input.measurement_date is not None:
        update_data["measurement_date"] = _input.measurement_date
    if _input.conditions is not None:
        update_data["conditions"] = _input.conditions

    daily_condition = await postgres.daily_condition.update(
        session, daily_condition_id, **update_data
    )
    if not daily_condition:
        return None

    return dto.UpdateDailyConditionOutput(id=daily_condition.id)
