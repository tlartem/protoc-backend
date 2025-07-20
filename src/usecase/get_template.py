import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def get_template(
    session: AsyncSession, template_id: uuid.UUID
) -> dto.GetTemplateOutput:
    template = await postgres.template.get(session, template_id)
    return dto.GetTemplateOutput(template=template)
