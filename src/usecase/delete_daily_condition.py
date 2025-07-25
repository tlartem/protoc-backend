import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src.adapter import postgres


async def delete_daily_condition(
    session: AsyncSession, daily_condition_id: uuid.UUID
) -> bool:
    return await postgres.daily_condition.delete(session, daily_condition_id)
