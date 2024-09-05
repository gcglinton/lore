from typing import Optional

from sqlmodel import Field, SQLModel
from sqlmodel import Column, TEXT


class Experiment_Tag__Base(SQLModel, table=True):
    __tablename__ = "experiment_tags"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = Field(default=None, sa_column=Column(TEXT))
    is_deleted: Optional[bool] = Field(default=0, index=hash)


class Experiment_Tag(SQLModel):
    id: int
    name: str
    description: Optional[str] = Field(default=None, sa_column=Column(TEXT))


class Experiment_Tag__Edit(SQLModel):
    name: str
    description: Optional[str] = Field(default=None, sa_column=Column(TEXT))
