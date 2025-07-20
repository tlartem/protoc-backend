import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def get_sheet(session: AsyncSession, sheet_id: uuid.UUID) -> dto.GetSheetOutput:
    sheet = await postgres.sheet.get(session, sheet_id)
    return dto.GetSheetOutput(sheet=sheet)
