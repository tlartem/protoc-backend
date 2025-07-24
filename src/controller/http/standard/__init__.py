from fastapi import APIRouter

standard_router = APIRouter(prefix="/standards", tags=["standards"])
from . import (
    create_standard,
    delete_standard,
    get_standard,
    get_standards,
    patch_standard,
)
