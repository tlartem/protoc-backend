from typing import TYPE_CHECKING

from sqlalchemy import JSONB
from sqlalchemy.orm import Mapped, relationship

from src import model

if TYPE_CHECKING:
    from .template import Template


class Sheet(model.Base):
    name: Mapped[str]
    cells: Mapped[JSONB]

    template: Mapped["Template"] = relationship(
        back_populates="sheets"
    )