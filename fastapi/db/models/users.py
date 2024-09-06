from typing import TYPE_CHECKING, Optional

from sqlmodel import Column, TEXT, SQLModel, Field, Relationship
from pydantic import EmailStr

from sqlalchemy import DateTime, func

import datetime

if TYPE_CHECKING:
    from db.models import Department__Base


class User__Base(SQLModel, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    name_first: str = Field(default=None)
    name_last: str = Field(default=None)
    email: Optional[EmailStr] = Field(default=None)
    phone: Optional[str] = Field(default=None)
    department: int = Field(foreign_key="departments.id")
    department_name: Optional["Department__Base"] = Relationship(back_populates="users")
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

    async def __admin_repr__(self, _):
        return f"{self.name_first} {self.name_last}"

    async def __admin_select2_repr__(self, _) -> str:
        from html import escape

        return f"<div><span>{escape(self.name_first + " " + self.name_last)}</span></div>"


class User(SQLModel):
    id: int
    username: str
    name_first: str = Field(default=None)
    name_last: str = Field(default=None)
    email: EmailStr = Field(default=None)
    phone: str = Field(default=None)
    department: int
    # created_at: float
    notes: str = Field(default=None, sa_column=Column(TEXT))
    is_legoteam: bool


class User__Edit(SQLModel):
    username: str
    name_first: Optional[str]
    name_last: Optional[str]
    email: EmailStr
    phone: Optional[str]
    department: int
    notes: Optional[str] = Field(default=None, sa_column=Column(TEXT))
    is_legoteam: Optional[bool]
