from fastapi import APIRouter

laboratory_router = APIRouter(prefix="/laboratories", tags=["laboratories"])

from . import get_laboratories, get_laboratory
