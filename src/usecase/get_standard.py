import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def get_standard(
    session: AsyncSession, standard_id: uuid.UUID
) -> dto.GetStandardOutput:
    standard = await postgres.standard.get(session, standard_id)
    return dto.GetStandardOutput(standard=standard)
