import uuid
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def get_files(
    session: AsyncSession, template_id: Optional[uuid.UUID] = None
) -> dto.GetFilesOutput:
    if template_id:
        files = await postgres.file.get_by_template(session, template_id)
    else:
        files = await postgres.file.get_all(session)
    return dto.GetFilesOutput(files=files)
