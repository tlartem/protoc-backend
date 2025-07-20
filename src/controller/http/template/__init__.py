from fastapi import APIRouter

template_router = APIRouter(prefix="/templates")
from . import create_template, get_templates, get_template, patch_template  # noqa
