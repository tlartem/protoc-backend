from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, model
from src.adapter import postgres


async def create_sheet(
    session: AsyncSession, _input: dto.CreateSheetInput
) -> dto.CreateSheetOutput:
    sheet = model.Sheet(
        name=_input.name,
        cells=_input.cells,
        template_id=_input.template_id,
    )
    await postgres.sheet.create(session, sheet)
    return dto.CreateSheetOutput(id=sheet.id)
