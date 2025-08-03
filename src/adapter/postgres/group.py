import logging
import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.model.group import Group

logger = logging.getLogger(__name__)


async def get(session: AsyncSession, group_id: uuid.UUID) -> Group | None:
    group = await session.get(Group, group_id)
    if not group:
        return None

    return group


async def get_all(session: AsyncSession) -> list[Group]:
    stmt = select(Group).order_by(Group.order, Group.name)
    result = await session.execute(stmt)
    groups = result.scalars().all()
    logger.info(f"Database query returned {len(groups)} groups")
    return list(groups)


async def create(session: AsyncSession, group: Group) -> Group:
    session.add(group)
    await session.commit()
    await session.refresh(group)

    return group


async def update(session: AsyncSession, group_id: uuid.UUID, **kwargs) -> Group | None:
    group = await session.get(Group, group_id)
    if not group:
        return None

    for key, value in kwargs.items():
        if value is not None:
            setattr(group, key, value)

    await session.commit()
    await session.refresh(group)

    return group


async def delete(session: AsyncSession, group_id: uuid.UUID) -> bool:
    group = await session.get(Group, group_id)
    if not group:
        return False

    await session.delete(group)
    await session.commit()

    logger.info(f"Deleted group with id: {group_id}")
    return True
