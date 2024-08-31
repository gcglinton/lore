from typing import Optional

from sqlmodel import Field, SQLModel
from sqlmodel import Column, TEXT


class Experiment_FundingSource__Base(SQLModel, table=True):
    __tablename__ = "experiment_fundingsource"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    name_short: Optional[str]
    description: Optional[str] = Field(sa_column=Column(TEXT))
    is_deleted: Optional[bool] = Field(default=0, index=hash)


class Experiment_FundingSource(SQLModel):
    id: int
    name: str
    name_short: Optional[str]
    description: Optional[str]


class Experiment_FundingSource__Edit(SQLModel):
    name: str
    name_short: Optional[str]
    description: Optional[str]
