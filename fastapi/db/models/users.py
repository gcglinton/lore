from typing import Optional

from sqlmodel import Field, SQLModel
from sqlmodel import Column, TEXT


class Users__Base(SQLModel, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    name_first: str
    name_last: str
    email: Optional[str]
    phone: Optional[str]
    sbda: int = Field(foreign_key="departments.id")
    # created_at: datetime.datetime = Field(
    #     sa_column_kwargs={
    #         "server_default": text("CURRENT_TIMESTAMP"),
    #     }
    # )
    notes: Optional[str] = Field(sa_column=Column(TEXT))
    is_legoteam: Optional[bool] = Field(default=0, index=hash)
    is_deleted: Optional[bool] = Field(default=0, index=hash)


class Users(SQLModel):
    id: int
    username: str
    name_first: str
    name_last: str
    email: str
    phone: str
    sbda: int
    # created_at: float
    notes: str
    is_legoteam: bool


class Users__Edit(SQLModel):
    username: str
    name_first: Optional[str]
    name_last: Optional[str]
    email: str
    phone: Optional[str]
    sbda: int
    notes: Optional[str]
    is_legoteam: Optional[bool]
