from typing import Optional

from sqlmodel import Field, SQLModel
from sqlmodel import Column, TEXT


class Experiment_AreaOfScience__Base(SQLModel, table=True):
    __tablename__ = "experiment_areaofscience"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = Field(sa_column=Column(TEXT))
    is_deleted: Optional[bool] = Field(default=0, index=hash)


class Experiment_AreaOfScience(SQLModel):
    id: int
    name: str
    description: Optional[str]


class Experiment_AreaOfScience__Edit(SQLModel):
    name: str
    description: Optional[str]
