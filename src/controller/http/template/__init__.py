from fastapi import APIRouter

template_router = APIRouter(prefix="/templates", tags=["templates"])
from . import (
    create_template,
    get_template,
    get_template_attributes,
    get_template_with_attributes,
    get_templates,
    patch_template,
    set_template_attributes,
)  # noqa
