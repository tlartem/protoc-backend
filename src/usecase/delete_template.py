import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def delete_template(
    template_id: uuid.UUID, session: AsyncSession
) -> dto.DeleteTemplateOutput:
    """Удаляет шаблон по ID"""
    success = await postgres.template.delete(session, template_id)

    if not success:
        raise ValueError(f"Template {template_id} not found")

    return dto.DeleteTemplateOutput(success=True, template_id=template_id)
