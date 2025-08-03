from pydantic import BaseModel


class DeleteGroupOutput(BaseModel):
    success: bool
