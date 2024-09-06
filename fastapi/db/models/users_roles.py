from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, SQLModel
from sqlmodel import Column, TEXT


class User_Role__Base(SQLModel, table=True):
    __tablename__ = "users_roles"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = Field(default=None, sa_column=Column(TEXT))
    is_deleted: Optional[bool] = Field(default=0, index=hash)


class User_Role(SQLModel):
    id: int
    name: str
    description: Optional[str] = Field(default=None, sa_column=Column(TEXT))


class User_Role__Edit(SQLModel):
    name: str
    description: Optional[str] = Field(default=None, sa_column=Column(TEXT))
