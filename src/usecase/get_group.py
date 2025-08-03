import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def get_group(session: AsyncSession, group_id: uuid.UUID) -> dto.GetGroupOutput:
    group = await postgres.group.get(session, group_id)
    return dto.GetGroupOutput(group=group)
