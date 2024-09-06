from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, SQLModel
from sqlmodel import Column, TEXT


class Experiment_Tag__Base(SQLModel, table=True):
    __tablename__ = "experiment_tags"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = Field(default=None, sa_column=Column(TEXT))
    is_deleted: Optional[bool] = Field(default=0, index=hash)

    async def __admin_repr__(self, _):
        return f"{self.name}"

    async def __admin_select2_repr__(self, _) -> str:
        from html import escape

        return f"<div><span>{escape(self.name)}</span></div>"


class Experiment_Tag(SQLModel):
    id: int
    name: str
    description: Optional[str] = Field(default=None, sa_column=Column(TEXT))


class Experiment_Tag__Edit(SQLModel):
    name: str
    description: Optional[str] = Field(default=None, sa_column=Column(TEXT))
