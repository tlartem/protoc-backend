from datetime import date
from typing import Optional

from fastapi import Depends, Query
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import daily_condition_router


@daily_condition_router.get("/")
async def get_daily_conditions(
    laboratory_id: Optional[UUID4] = Query(None, description="Фильтр по laboratory_id"),
    start_date: Optional[date] = Query(None, description="Начальная дата фильтра"),
    end_date: Optional[date] = Query(None, description="Конечная дата фильтра"),
    session: AsyncSession = Depends(get_session),
) -> dto.GetDailyConditionsOutput:
    return await usecase.get_daily_conditions(
        session, laboratory_id, start_date, end_date
    )
