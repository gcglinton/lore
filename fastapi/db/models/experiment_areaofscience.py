from typing import Optional

from sqlmodel import Field, SQLModel, Relationship
from sqlmodel import Column, TEXT

# from .experiments import Experiments__Base


class Experiment_AreaOfScience__Base(SQLModel, table=True):
    __tablename__ = "experiment_areaofscience"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = Field(default=None, sa_column=Column(TEXT))
    is_deleted: Optional[bool] = Field(default=0, index=hash)

    experiments: list["Experiment__Base"] = Relationship(back_populates="area_of_science_name")


class Experiment_AreaOfScience(SQLModel):
    id: int
    name: str
    description: Optional[str] = Field(default=None, sa_column=Column(TEXT))


class Experiment_AreaOfScience__Edit(SQLModel):
    name: str
    description: Optional[str] = Field(default=None, sa_column=Column(TEXT))
