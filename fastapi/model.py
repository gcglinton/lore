from typing import Optional
import datetime

from sqlmodel import Field, SQLModel, create_engine

from sqlmodel import Column, TEXT, DateTime, VARBINARY, text

from sqlmodel import func, Relationship


engine = create_engine("sqlite:///db.sqlite3")



class Experiment_Status__Base(SQLModel, table=True):
    __tablename__ = "experiment_statuses"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = Field(sa_column=Column(TEXT))
    is_deleted: Optional[bool] = Field(default=0, index=hash)


class Experiment_Status(SQLModel):
    id: int
    name: str
    description: Optional[str]

class Experiment_Status__Edit(SQLModel):
    name: str
    description: Optional[str]



class Experiment_LevelOfEffort__Base(SQLModel, table=True):
    __tablename__ = "experiment_levelofeffort"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = Field(sa_column=Column(TEXT))
    is_deleted: Optional[bool] = Field(default=0, index=hash)

class Experiment_LevelOfEffort(SQLModel):
    id: int
    name: str
    description: Optional[str]

class Experiment_LevelOfEffort__Edit(SQLModel):
    name: str
    description: Optional[str]



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



class Experiment_Tags__Base(SQLModel, table=True):
    __tablename__ = "experiment_tags"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = Field(sa_column=Column(TEXT))
    is_deleted: Optional[bool] = Field(default=0, index=hash)

class Experiment_Tags(SQLModel):
    id: int
    name: str
    description: Optional[str]

class Experiment_Tags__Edit(SQLModel):
    name: str
    description: Optional[str]



class Experiment_AreaOfScience__Base(SQLModel, table=True):
    __tablename__ = "experiment_areaofscience"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = Field(sa_column=Column(TEXT))
    is_deleted: Optional[bool] = Field(default=0, index=hash)

class Experiment_AreaOfScience(SQLModel):
    id: int
    name: str
    description: Optional[str]

class Experiment_AreaOfScience__Edit(SQLModel):
    name: str
    description: Optional[str]


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
    is_deleted: bool

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
    #created_at: float
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