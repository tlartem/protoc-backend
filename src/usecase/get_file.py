import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def get_file(session: AsyncSession, file_id: uuid.UUID) -> dto.GetFileOutput:
    file = await postgres.file.get(session, file_id)
    return dto.GetFileOutput(file=file)
