from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, model
from src.adapter import postgres


async def create_daily_condition(
    session: AsyncSession, _input: dto.CreateDailyConditionInput
) -> dto.CreateDailyConditionOutput:
    # Проверяем, что лаборатория существует
    laboratory = await postgres.laboratory.get(session, _input.laboratory_id)
    if not laboratory:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Laboratory not found"
        )

    daily_condition = model.DailyCondition(
        laboratory_id=_input.laboratory_id,
        measurement_date=_input.measurement_date,
        conditions=_input.conditions,
    )

    created_condition = await postgres.daily_condition.create(session, daily_condition)
    return dto.CreateDailyConditionOutput(id=created_condition.id)
