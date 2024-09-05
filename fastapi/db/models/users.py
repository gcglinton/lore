from typing import Optional

from sqlmodel import Field, SQLModel
from sqlmodel import Column, TEXT

from sqlalchemy import DateTime, func

import datetime


class User__Base(SQLModel, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    name_first: str = Field(default=None)
    name_last: str = Field(default=None)
    email: Optional[str] = Field(default=None)
    phone: Optional[str] = Field(default=None)
    department: int = Field(foreign_key="departments.id")
    created_at: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
    )
    # created_at: datetime.datetime = Field(
    #     sa_column_kwargs={
    #         "server_default": text("CURRENT_TIMESTAMP"),
    #     }
    # )
    notes: Optional[str] = Field(default=None, sa_column=Column(TEXT))
    is_legoteam: Optional[bool] = Field(default=0, index=hash)
    is_deleted: Optional[bool] = Field(default=0, index=hash)


class User(SQLModel):
    id: int
    username: str
    name_first: str = Field(default=None)
    name_last: str = Field(default=None)
    email: str = Field(default=None)
    phone: str = Field(default=None)
    department: int
    # created_at: float
    notes: str = Field(default=None, sa_column=Column(TEXT))
    is_legoteam: bool


class User__Edit(SQLModel):
    username: str
    name_first: Optional[str]
    name_last: Optional[str]
    email: str
    phone: Optional[str]
    department: int
    notes: Optional[str] = Field(default=None, sa_column=Column(TEXT))
    is_legoteam: Optional[bool]
