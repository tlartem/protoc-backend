from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src import model

if TYPE_CHECKING:
    from .condition_type import ConditionType
    from .daily_condition import DailyCondition

# Промежуточная таблица для связи многие-ко-многим между Laboratory и ConditionType
laboratory_condition_type = Table(
    "laboratory_condition_type",
    model.Base.metadata,
    Column("laboratory_id", ForeignKey("laboratorys.id"), primary_key=True),
    Column("condition_type_id", ForeignKey("conditiontypes.id"), primary_key=True),
)


class Laboratory(model.Base):
    name: Mapped[str] = mapped_column()

    # Связь многие ко многим с ConditionType
    condition_types: Mapped[list["ConditionType"]] = relationship(
        secondary=laboratory_condition_type,
        back_populates="laboratories",
        lazy="select",
    )

    # Связь один ко многим с DailyCondition
    daily_conditions: Mapped[list["DailyCondition"]] = relationship(
        back_populates="laboratory", cascade="all, delete-orphan"
    )
