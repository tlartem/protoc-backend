import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def delete_group(session: AsyncSession, group_id: uuid.UUID) -> dto.DeleteGroupOutput:
    success = await postgres.group.delete(session, group_id)
    return dto.DeleteGroupOutput(success=success)
