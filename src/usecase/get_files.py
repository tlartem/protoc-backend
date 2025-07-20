from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def get_files(session: AsyncSession) -> dto.GetFilesOutput:
    files = await postgres.file.get_all(session)
    return dto.GetFilesOutput(files=files)
