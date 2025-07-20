import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def patch_template(
    session: AsyncSession, template_id: uuid.UUID, _input: dto.PatchTemplateInput
) -> dto.PatchTemplateOutput | None:
    update_data = {}
    if _input.name is not None:
        update_data["name"] = _input.name
    if _input.description is not None:
        update_data["description"] = _input.description
    if _input.elements is not None:
        update_data["elements"] = _input.elements

    template = await postgres.template.update(session, template_id, **update_data)
    if not template:
        return None

    return dto.PatchTemplateOutput(id=template.id)
