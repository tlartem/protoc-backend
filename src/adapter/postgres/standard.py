import logging
import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.model.standard import Standard

logger = logging.getLogger(__name__)


async def get(session: AsyncSession, standard_id: uuid.UUID) -> Standard | None:
    standard = await session.get(Standard, standard_id)
    if not standard:
        return None

    return standard


async def get_all(session: AsyncSession) -> list[Standard]:
    stmt = select(Standard)
    result = await session.execute(stmt)
    standards = result.scalars().all()
    logger.info(f"Database query returned {len(standards)} standards")
    return standards


async def create(session: AsyncSession, standard: Standard) -> Standard:
    session.add(standard)
    await session.commit()
    await session.refresh(standard)

    return standard


async def update(
    session: AsyncSession, standard_id: uuid.UUID, **kwargs
) -> Standard | None:
    standard = await session.get(Standard, standard_id)
    if not standard:
        return None

    for key, value in kwargs.items():
        if value is not None:
            setattr(standard, key, value)

    await session.commit()
    await session.refresh(standard)

    return standard


async def delete(session: AsyncSession, standard_id: uuid.UUID) -> bool:
    standard = await session.get(Standard, standard_id)
    if not standard:
        return False

    await session.delete(standard)
    await session.commit()
    return True
