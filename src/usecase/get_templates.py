from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def get_templates(session: AsyncSession) -> dto.GetTemplatesOutput:
    templates = await postgres.template.get_all(session)
    return dto.GetTemplatesOutput(templates=templates)
