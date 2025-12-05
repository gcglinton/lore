from typing import TYPE_CHECKING, Optional

from sqlmodel import TEXT, Column, Field, Relationship, SQLModel

if TYPE_CHECKING:
    from db.models import Experiment__Base


class Experiment_LevelOfEffort__Base(SQLModel, table=True):
    __tablename__ = "experiment_levelofeffort"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = Field(default=None, sa_column=Column(TEXT))
    is_deleted: Optional[bool] = Field(default=0, index=hash)

    experiments: list["Experiment__Base"] = Relationship(
        back_populates="level_of_effort_name"
    )

    async def __admin_repr__(self, _):
        return f"{self.name}"

    async def __admin_select2_repr__(self, _) -> str:
        from html import escape

        return f"<div><span>{escape(self.name)}</span></div>"


class Experiment_LevelOfEffort(SQLModel):
    id: int
    name: str
    description: Optional[str] = Field(default=None, sa_column=Column(TEXT))


class Experiment_LevelOfEffort__Edit(SQLModel):
    name: str
    description: Optional[str] = Field(default=None, sa_column=Column(TEXT))
