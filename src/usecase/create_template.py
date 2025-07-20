from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, model
from src.adapter import postgres


async def create_template(
    session: AsyncSession, _input: dto.CreateTemplateInput
) -> dto.CreateTemplateOutput:
    template = model.Template(
        name=_input.name,
        description=_input.description,
        elements=_input.elements,
    )
    await postgres.template.create(session, template)
    return dto.CreateTemplateOutput(id=template.id)
