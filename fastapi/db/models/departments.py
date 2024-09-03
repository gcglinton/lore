from typing import Optional

from sqlmodel import Field, SQLModel
from sqlmodel import Column, TEXT


class Departments__Base(SQLModel, table=True):
    __tablename__ = "departments"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    acronym: str
    environment_code: str = Field(max_length=2)
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
    description: Optional[str] = Field(sa_column=Column(TEXT))
    is_science: Optional[bool] = Field(default=0, index=hash)
    is_deleted: Optional[bool] = Field(default=0, index=hash)


class Departments(SQLModel):
    id: int
    name: str
    acronym: str
    environment_code: str
    cio_name: str
    cio_name: str
    cio_email: str
    cloud_dg_name: str
    cloud_dg_email: str
    aom_name: str
    aom_email: str
    client_exec_name: str
    client_exec_email: str
    sdm_name: str
    sdm_email: str
    description: str
    is_science: bool


class Departments__Edit(SQLModel):
    name: str
    acronym: str
    environment_code: str = Field(max_length=2)
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
    is_science: Optional[bool]
