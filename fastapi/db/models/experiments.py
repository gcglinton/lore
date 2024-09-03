# Table experiments {
#   id integer [primary key, increment]
#   name varchar
#   status integer [ref: > experiments_statuses.id]
#   created_ts timestamp [default: `now()`]
#   created_user integer [ref: > users.id]
#   delegated bool [default: false]
#   sbda integer [ref: > departments.id]
#   research_initiative integer
#   area_of_science integer [ref: > experiments_areasofscience.id]
#   background text
#   description text
#   goals text
#   level_of_effort integer [ref: > experiments_levelofeffort.id, default: 3]
#   cloud_provider_requested integer [ref: - cloud_providers.id]
#   cloud_provider_actual integer [ref: - cloud_providers.id]
#   forcasted_end date [default: `now()`]
#   fin_forecasted float
#   fin_initial float
#   fin_actual float [default: 0.0]
#   last_updated timestamp [default: `now()`]
#   fin_automated_reports bool [default: false]
#   environment_name varchar
#   funding_source integer [ref: > experiments_fundingsource.id]
#   data_sensivitity integer [ref: > experiments_datasensitivity.id]
#   progress integer [default: 0]
#   is_deleted bool [default: 0]
#   is_archived bool [default: 0]

#   indexes {
#     status
#     (is_deleted, is_archived)
#   }
# }

from typing import Optional

from sqlmodel import Field, SQLModel
from sqlmodel import Column, TEXT


class Experiments__Base(SQLModel, table=True):
    __tablename__ = "experiments"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    status: Optional[int] = Field(foreign_key="experiment_statuses.id", index=hash)
    # created_at: datetime.datetime = Field(
    #     sa_column_kwargs={
    #         "server_default": text("CURRENT_TIMESTAMP"),
    #     }
    # )
    created_user: int = Field(foreign_key="users.id")
    delegated: Optional[bool] = Field(default=0)
    department: int = Field(foreign_key="departments.id")
    research_initiative: Optional[int]
    area_of_science: Optional[int] = Field(foreign_key="experiment_areaofscience.id")
    level_of_effort: Optional[int] = Field(foreign_key="experiment_levelofeffort.id")
    funding_source: Optional[int] = Field(foreign_key="experiment_fundingsource.id")
    data_sensivitity: Optional[int] = Field(foreign_key="experiment_datasensitivity.id")
    cloud_provider_requested: Optional[int] = Field(foreign_key="cloud_providers.id")
    cloud_provider_actual: Optional[int] = Field(foreign_key="cloud_providers.id")
    background: Optional[str] = Field(sa_column=Column(TEXT))
    description: Optional[str] = Field(sa_column=Column(TEXT))
    goals: Optional[str] = Field(sa_column=Column(TEXT))
    fin_forecasted: Optional[float] = Field(default=0.0)
    fin_initial: Optional[float] = Field(default=0.0)
    fin_actual: Optional[float] = Field(default=0.0)
    fin_automated_reports: Optional[bool] = Field(default=0, index=hash)
    #   last_updated timestamp [default: `now()`]
    progress: Optional[int] = Field(default=0)
    environment_name: Optional[str]
    is_deleted: Optional[bool] = Field(default=0, index=hash)
    is_archived: Optional[bool] = Field(default=0, index=hash)


class Experiments(SQLModel):
    id: Optional[int]
    name: str
    status: Optional[int]
    # created_at: datetime.datetime = Field(
    #     sa_column_kwargs={
    #         "server_default": text("CURRENT_TIMESTAMP"),
    #     }
    # )
    created_user: int
    delegated: bool
    department: int
    research_initiative: Optional[int]
    area_of_science: Optional[int]
    level_of_effort: Optional[int]
    funding_source: Optional[int]
    data_sensivitity: Optional[int]
    cloud_provider_requested: Optional[int]
    cloud_provider_actual: Optional[int]
    background: Optional[str]
    description: Optional[str]
    goals: Optional[str]
    fin_forecasted: Optional[float]
    fin_initial: Optional[float]
    fin_actual: Optional[float]
    fin_automated_reports: Optional[bool]
    # last_updated: Optional[timestamp]
    progress: Optional[int]
    environment_name: Optional[str]
    is_archived: Optional[bool]


class Experiments__Edit(SQLModel):
    name: str
    status: Optional[int]
    # created_at: datetime.datetime = Field(
    #     sa_column_kwargs={
    #         "server_default": text("CURRENT_TIMESTAMP"),
    #     }
    # )
    delegated: bool
    department: int
    research_initiative: Optional[int]
    area_of_science: Optional[int]
    level_of_effort: Optional[int]
    funding_source: Optional[int]
    data_sensivitity: Optional[int]
    cloud_provider_requested: Optional[int]
    cloud_provider_actual: Optional[int]
    background: Optional[str]
    description: Optional[str]
    goals: Optional[str]
    fin_forecasted: Optional[float]
    fin_initial: Optional[float]
    fin_actual: Optional[float]
    fin_automated_reports: Optional[bool]
    environment_name: Optional[str]
    progress: Optional[int]
