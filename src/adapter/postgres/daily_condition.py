import logging
import uuid
from datetime import date
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.model.daily_condition import DailyCondition

logger = logging.getLogger(__name__)


async def get(
    session: AsyncSession, daily_condition_id: uuid.UUID
) -> DailyCondition | None:
    daily_condition = await session.get(DailyCondition, daily_condition_id)
    return daily_condition


async def get_all(session: AsyncSession) -> list[DailyCondition]:
    stmt = select(DailyCondition)
    result = await session.execute(stmt)
    daily_conditions = result.scalars().all()

    logger.info(f"Database query returned {len(daily_conditions)} daily conditions")
    return daily_conditions


async def get_by_laboratory(
    session: AsyncSession, laboratory_id: uuid.UUID
) -> list[DailyCondition]:
    stmt = select(DailyCondition).where(DailyCondition.laboratory_id == laboratory_id)
    result = await session.execute(stmt)
    daily_conditions = result.scalars().all()

    logger.info(
        f"Found {len(daily_conditions)} daily conditions for laboratory {laboratory_id}"
    )
    return daily_conditions


async def get_by_date_range(
    session: AsyncSession,
    laboratory_id: Optional[uuid.UUID] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
) -> list[DailyCondition]:
    stmt = select(DailyCondition)

    if laboratory_id:
        stmt = stmt.where(DailyCondition.laboratory_id == laboratory_id)
    if start_date:
        stmt = stmt.where(DailyCondition.measurement_date >= start_date)
    if end_date:
        stmt = stmt.where(DailyCondition.measurement_date <= end_date)

    result = await session.execute(stmt)
    daily_conditions = result.scalars().all()

    logger.info(f"Found {len(daily_conditions)} daily conditions in date range")
    return daily_conditions


async def create(
    session: AsyncSession, daily_condition: DailyCondition
) -> DailyCondition:
    session.add(daily_condition)
    await session.commit()
    await session.refresh(daily_condition)

    logger.info(
        f"Created daily condition for laboratory {daily_condition.laboratory_id} on {daily_condition.measurement_date}"
    )
    return daily_condition


async def update(
    session: AsyncSession, daily_condition_id: uuid.UUID, **kwargs
) -> DailyCondition | None:
    daily_condition = await session.get(DailyCondition, daily_condition_id)
    if not daily_condition:
        return None

    for key, value in kwargs.items():
        if value is not None:
            setattr(daily_condition, key, value)

    await session.commit()
    await session.refresh(daily_condition)

    logger.info(f"Updated daily condition {daily_condition_id}")
    return daily_condition


async def delete(session: AsyncSession, daily_condition_id: uuid.UUID) -> bool:
    daily_condition = await session.get(DailyCondition, daily_condition_id)
    if not daily_condition:
        return False

    await session.delete(daily_condition)
    await session.commit()

    logger.info(f"Deleted daily condition with id: {daily_condition_id}")
    return True
