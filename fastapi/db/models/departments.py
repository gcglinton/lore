from typing import Optional

from sqlmodel import SQLModel, Field, Relationship
from sqlmodel import Column, TEXT


class Department__Base(SQLModel, table=True):
    __tablename__ = "departments"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    acronym: str
    environment_code: str = Field(max_length=2)
    cio_name: Optional[str] = Field(default=None)
    cio_name: Optional[str] = Field(default=None)
    cio_email: Optional[str] = Field(default=None)
    cloud_dg_name: Optional[str] = Field(default=None)
    cloud_dg_email: Optional[str] = Field(default=None)
    aom_name: Optional[str] = Field(default=None)
    aom_email: Optional[str] = Field(default=None)
    client_exec_name: Optional[str] = Field(default=None)
    client_exec_email: Optional[str] = Field(default=None)
    sdm_name: Optional[str] = Field(default=None)
    sdm_email: Optional[str] = Field(default=None)
    description: Optional[str] = Field(sa_column=Column(TEXT))
    is_science: Optional[bool] = Field(default=0, index=hash)
    is_deleted: Optional[bool] = Field(default=0, index=hash)

    users: list["User__Base"] = Relationship(back_populates="department_name")

    async def __admin_repr__(self, _):
        return f"{self.name} ({self.acronym})"

    async def __admin_select2_repr__(self, _) -> str:
        from html import escape

        return f"<div><span>{escape(f"{self.name} ({self.acronym})")}</span></div>"


class Department(SQLModel):
    id: int
    name: str
    acronym: str
    environment_code: str
    cio_name: Optional[str]
    cio_name: Optional[str]
    cio_email: Optional[str]
    cloud_dg_name: Optional[str]
    cloud_dg_email: Optional[str]
    aom_name: Optional[str]
    aom_email: Optional[str]
    client_exec_name: Optional[str]
    client_exec_email: Optional[str]
    sdm_name: Optional[str]
    sdm_email: Optional[str]
    description: Optional[str]
    is_science: bool


class Department__Edit(SQLModel):
    name: str
    acronym: str
    environment_code: str = Field(max_length=2)
    cio_name: Optional[str] = Field(default=None)
    cio_name: Optional[str] = Field(default=None)
    cio_email: Optional[str] = Field(default=None)
    cloud_dg_name: Optional[str] = Field(default=None)
    cloud_dg_email: Optional[str] = Field(default=None)
    aom_name: Optional[str] = Field(default=None)
    aom_email: Optional[str] = Field(default=None)
    client_exec_name: Optional[str] = Field(default=None)
    client_exec_email: Optional[str] = Field(default=None)
    sdm_name: Optional[str] = Field(default=None)
    sdm_email: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    is_science: Optional[bool] = Field(default=False)
