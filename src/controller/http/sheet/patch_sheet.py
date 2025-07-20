from fastapi import Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import sheet_router


@sheet_router.patch("/{sheet_id}")
async def patch_sheet(
    sheet_id: UUID4,
    input: dto.PatchSheetInput,
    session: AsyncSession = Depends(get_session),
) -> dto.PatchSheetOutput:
    result = await usecase.patch_sheet(session, sheet_id, input)
    if not result:
        raise HTTPException(status_code=404, detail="Sheet not found")
    return result
