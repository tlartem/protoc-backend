from typing import Any

from pydantic import UUID4, BaseModel, ConfigDict


class CreateProtocolInput(BaseModel):
    template_id: UUID4
    file_id: UUID4
    cells_to_update: dict[str, Any]
    print_area: str

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "template_id": "123e4567-e89b-12d3-a456-426614174000",
                    "file_id": "123e4567-e89b-12d3-a456-426614174111",
                    "cells_to_update": {"A2": "value1", "B2": "value2", "C2": 123},
                    "print_area": "A1:C10",
                }
            ]
        }
    )


class CreateProtocolOutput(BaseModel):
    protocol_id: UUID4
    file_content: bytes
