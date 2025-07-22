from fastapi import Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import attribute_router


@attribute_router.get("/{attribute_id}/values")
async def get_attribute_values(
    attribute_id: UUID4,
    session: AsyncSession = Depends(get_session),
) -> dto.GetAttributeValuesOutput:
    result = await usecase.get_attribute_values(session, attribute_id)
    if not result:
        raise HTTPException(status_code=404, detail="Attribute not found")
    return result
