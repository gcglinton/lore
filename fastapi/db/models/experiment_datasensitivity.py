from typing import TYPE_CHECKING, Optional

from sqlmodel import SQLModel, Field, Relationship
from sqlmodel import Column, TEXT

if TYPE_CHECKING:
    from db.models import Experiment__Base


class Experiment_DataSensitivity__Base(SQLModel, table=True):
    __tablename__ = "experiment_datasensitivity"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = Field(default=None, sa_column=Column(TEXT))
    is_deleted: Optional[bool] = Field(default=0, index=hash)

    experiments: list["Experiment__Base"] = Relationship(back_populates="data_sensivitity_name")

    async def __admin_repr__(self, _):
        return f"{self.name}"

    async def __admin_select2_repr__(self, _) -> str:
        from html import escape

        return f"<div><span>{escape(self.name)}</span></div>"


class Experiment_DataSensitivity(SQLModel):
    id: int
    name: str
    description: Optional[str] = Field(default=None, sa_column=Column(TEXT))


class Experiment_DataSensitivity__Edit(SQLModel):
    name: str
    description: Optional[str] = Field(default=None, sa_column=Column(TEXT))
