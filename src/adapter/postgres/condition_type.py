import logging
import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.model.condition_type import ConditionType

logger = logging.getLogger(__name__)


async def get(
    session: AsyncSession, condition_type_id: uuid.UUID
) -> ConditionType | None:
    condition_type = await session.get(ConditionType, condition_type_id)
    return condition_type


async def get_all(session: AsyncSession) -> list[ConditionType]:
    stmt = select(ConditionType)
    result = await session.execute(stmt)
    condition_types = result.scalars().all()

    logger.info(f"Database query returned {len(condition_types)} condition types")
    return condition_types


async def create(session: AsyncSession, condition_type: ConditionType) -> ConditionType:
    session.add(condition_type)
    await session.commit()
    await session.refresh(condition_type)

    logger.info(f"Created condition type: {condition_type.name}")
    return condition_type


async def update(
    session: AsyncSession, condition_type_id: uuid.UUID, **kwargs
) -> ConditionType | None:
    condition_type = await session.get(ConditionType, condition_type_id)
    if not condition_type:
        return None

    for key, value in kwargs.items():
        if value is not None:
            setattr(condition_type, key, value)

    await session.commit()
    await session.refresh(condition_type)

    logger.info(f"Updated condition type: {condition_type.name}")
    return condition_type


async def delete(session: AsyncSession, condition_type_id: uuid.UUID) -> bool:
    condition_type = await session.get(ConditionType, condition_type_id)
    if not condition_type:
        return False

    await session.delete(condition_type)
    await session.commit()

    logger.info(f"Deleted condition type with id: {condition_type_id}")
    return True
