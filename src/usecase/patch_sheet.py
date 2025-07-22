import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def patch_sheet(
    session: AsyncSession, sheet_id: uuid.UUID, _input: dto.PatchSheetInput
) -> dto.PatchSheetOutput | None:
    print("patch_sheet", _input)
    update_data = {}
    if _input.name is not None:
        update_data["name"] = _input.name
    if _input.cells is not None:
        update_data["cells"] = _input.cells

    sheet = await postgres.sheet.update(session, sheet_id, **update_data)
    if not sheet:
        return None

    return dto.PatchSheetOutput(id=sheet.id)
