import uuid
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def get_sheets(
    session: AsyncSession, template_id: Optional[uuid.UUID] = None
) -> dto.GetSheetsOutput:
    if template_id:
        sheets = await postgres.sheet.get_by_template(session, template_id)
    else:
        sheets = await postgres.sheet.get_all(session)
    return dto.GetSheetsOutput(sheets=sheets)
