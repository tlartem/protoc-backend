import logging
import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.model.laboratory import Laboratory

logger = logging.getLogger(__name__)


async def get(session: AsyncSession, laboratory_id: uuid.UUID) -> Laboratory | None:
    # Используем selectinload для загрузки связанных condition_types
    stmt = (
        select(Laboratory)
        .options(selectinload(Laboratory.condition_types))
        .where(Laboratory.id == laboratory_id)
    )
    result = await session.execute(stmt)
    laboratory = result.scalar_one_or_none()

    if laboratory:
        logger.info(
            f"Found laboratory {laboratory.name} with {len(laboratory.condition_types)} condition types"
        )

    return laboratory


async def get_all(session: AsyncSession) -> list[Laboratory]:
    # Загружаем все лаборатории с их типами условий
    stmt = select(Laboratory).options(selectinload(Laboratory.condition_types))
    result = await session.execute(stmt)
    laboratories = result.scalars().unique().all()

    logger.info(f"Database query returned {len(laboratories)} laboratories")
    for lab in laboratories:
        logger.info(
            f"Laboratory {lab.name} has {len(lab.condition_types)} condition types"
        )

    return laboratories


async def create(session: AsyncSession, laboratory: Laboratory) -> Laboratory:
    session.add(laboratory)
    await session.commit()
    await session.refresh(laboratory)

    logger.info(f"Created laboratory: {laboratory.name}")
    return laboratory


async def update(
    session: AsyncSession, laboratory_id: uuid.UUID, **kwargs
) -> Laboratory | None:
    laboratory = await session.get(Laboratory, laboratory_id)
    if not laboratory:
        return None

    for key, value in kwargs.items():
        if value is not None:
            setattr(laboratory, key, value)

    await session.commit()
    await session.refresh(laboratory)

    logger.info(f"Updated laboratory: {laboratory.name}")
    return laboratory


async def delete(session: AsyncSession, laboratory_id: uuid.UUID) -> bool:
    laboratory = await session.get(Laboratory, laboratory_id)
    if not laboratory:
        return False

    await session.delete(laboratory)
    await session.commit()

    logger.info(f"Deleted laboratory with id: {laboratory_id}")
    return True
