from fastapi import APIRouter

group_router = APIRouter(prefix="/groups", tags=["groups"])
from . import create_group, delete_group, get_group, get_groups, patch_group  # noqa
