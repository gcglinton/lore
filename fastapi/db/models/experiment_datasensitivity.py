from typing import Optional

from sqlmodel import Field, SQLModel
from sqlmodel import Column, TEXT


class Experiment_DataSensitivity__Base(SQLModel, table=True):
    __tablename__ = "experiment_datasensitivity"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = Field(sa_column=Column(TEXT))
    is_deleted: Optional[bool] = Field(default=0, index=hash)


class Experiment_DataSensitivity(SQLModel):
    id: int
    name: str
    description: Optional[str]


class Experiment_DataSensitivity__Edit(SQLModel):
    name: str
    description: Optional[str]
