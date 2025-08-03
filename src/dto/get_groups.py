from pydantic import BaseModel

from .get_group import Group


class GetGroupsOutput(BaseModel):
    groups: list[Group]

    class Config:
        from_attributes = True
