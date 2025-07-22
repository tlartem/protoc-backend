import logging
import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.model.attribute import Attribute

logger = logging.getLogger(__name__)


async def get_all(session: AsyncSession) -> list[Attribute]:
    stmt = select(Attribute)
    result = await session.execute(stmt)
    attributes = result.scalars().all()
    logger.info(f"Database query returned {len(attributes)} attributes")
    return attributes


async def create(session: AsyncSession, attribute: Attribute) -> Attribute:
    session.add(attribute)
    await session.commit()
    await session.refresh(attribute)

    return attribute


async def get_by_name(session: AsyncSession, name: str) -> Attribute | None:
    stmt = select(Attribute).where(Attribute.name == name)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()


async def get_by_id(session: AsyncSession, attribute_id: uuid.UUID) -> Attribute | None:
    """Получает атрибут по ID"""
    attribute = await session.get(Attribute, attribute_id)
    return attribute
