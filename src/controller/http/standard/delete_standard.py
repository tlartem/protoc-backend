from fastapi import Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src import usecase
from src.adapter.postgres import get_session

from . import standard_router


@standard_router.delete("/{standard_id}")
async def delete_standard(
    standard_id: UUID4,
    session: AsyncSession = Depends(get_session),
) -> dict[str, str]:
    success = await usecase.delete_standard(session, standard_id)
    if not success:
        raise HTTPException(status_code=404, detail="Standard not found")
    return {"message": "Standard deleted successfully"}
