import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src.adapter import postgres


async def delete_standard(session: AsyncSession, standard_id: uuid.UUID) -> bool:
    return await postgres.standard.delete(session, standard_id)
