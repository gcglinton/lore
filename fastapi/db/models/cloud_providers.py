from typing import Optional

from sqlmodel import Field, SQLModel
from sqlmodel import Column, TEXT


class Cloud_Providers__Base(SQLModel, table=True):
    __tablename__ = "cloud_providers"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    name_short: str
    contact_name: Optional[str]
    contact_email: Optional[str]
    contact_phone: Optional[str]
    description: Optional[str] = Field(sa_column=Column(TEXT))
    is_deleted: Optional[bool] = Field(default=0, index=hash)


class Cloud_Providers(SQLModel):
    id: int
    name: str
    name_short: str
    contact_name: str
    contact_email: str
    contact_phone: str
    description: str


class Cloud_Providers__Edit(SQLModel):
    name: str
    name_short: str
    contact_name: Optional[str]
    contact_email: Optional[str]
    contact_phone: Optional[str]
    description: Optional[str]
