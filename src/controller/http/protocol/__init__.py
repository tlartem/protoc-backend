from fastapi import APIRouter

protocol_router = APIRouter(prefix="/protocols", tags=["protocols"])
from . import create_protocol  # noqa
