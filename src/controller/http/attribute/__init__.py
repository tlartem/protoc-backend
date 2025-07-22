from fastapi import APIRouter

attribute_router = APIRouter(prefix="/attributes", tags=["attributes"])

from . import create_attribute, get_attribute_values, get_attributes
