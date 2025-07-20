from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def get_sheets(session: AsyncSession) -> dto.GetSheetsOutput:
    sheets = await postgres.sheet.get_all(session)
    return dto.GetSheetsOutput(sheets=sheets)
