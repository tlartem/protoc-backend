from fastapi import APIRouter

template_router = APIRouter(prefix="/templates", tags=["templates"])
from . import (
    create_template,
    get_template,
    get_templates,
    patch_template,
)
