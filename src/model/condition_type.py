from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src import model

if TYPE_CHECKING:
    from .laboratory import Laboratory, laboratory_condition_type


class ConditionType(model.Base):
    name: Mapped[str] = mapped_column()
    unit: Mapped[str] = mapped_column()

    # Связь многие ко многим с Laboratory
    laboratories: Mapped[list["Laboratory"]] = relationship(
        secondary="laboratory_condition_type",
        back_populates="condition_types",
        lazy="select",
    )
