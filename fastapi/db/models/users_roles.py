from typing import Optional

from sqlmodel import Field, SQLModel
from sqlmodel import Column, TEXT


class Users_Roles__Base(SQLModel, table=True):
    __tablename__ = "users_roles"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = Field(sa_column=Column(TEXT))
    is_deleted: Optional[bool] = Field(default=0, index=hash)


class Users_Roles(SQLModel):
    id: int
    name: str
    description: Optional[str]


class Users_Roles__Edit(SQLModel):
    name: str
    description: Optional[str]
