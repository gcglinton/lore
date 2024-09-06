from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, SQLModel
from sqlmodel import Column, TEXT, Relationship

from sqlalchemy import DateTime, func
from sqlalchemy.orm import relationship as sa_relationship

import datetime

if TYPE_CHECKING:
    from db.models import Department__Base
    from db.models import Experiment_AreaOfScience__Base, Experiment_DataSensitivity__Base, Experiment_Status__Base

class Experiment__Base(SQLModel, table=True):
    __tablename__ = "experiments"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    status: Optional[int] = Field(default=None, foreign_key="experiment_statuses.id", index=hash)
    created_at: datetime.datetime = Field(
        default_factory=datetime.datetime.utcnow,
    )
    updated_at: Optional[datetime.datetime] = Field(
        default_factory=datetime.datetime.utcnow,
        sa_column=Column(DateTime(), onupdate=func.now()),
    )
    created_user: Optional[int] = Field(foreign_key="users.id")
    delegated: Optional[bool] = Field(default=0)
    department: int = Field(foreign_key="departments.id")
    research_initiative: Optional[int] = Field(default=None)
    level_of_effort: Optional[int] = Field(foreign_key="experiment_levelofeffort.id")
    funding_source: Optional[int] = Field(default=None, foreign_key="experiment_fundingsource.id")
    data_sensivitity: Optional[int] = Field(
        default=None, foreign_key="experiment_datasensitivity.id"
    )
    cloud_provider_requested: Optional[int] = Field(default=None, foreign_key="cloud_providers.id")
    cloud_provider_actual: Optional[int] = Field(default=None, foreign_key="cloud_providers.id")
    background: Optional[str] = Field(default=None, sa_column=Column(TEXT))
    description: Optional[str] = Field(default=None, sa_column=Column(TEXT))
    goals: Optional[str] = Field(default=None, sa_column=Column(TEXT))
    fin_forecasted: Optional[float] = Field(default=0.0)
    fin_initial: Optional[float] = Field(default=0.0)
    fin_actual: Optional[float] = Field(default=0.0)
    fin_automated_reports: Optional[bool] = Field(default=False, index=hash)
    lego_evo_lead: Optional[int] = Field(default=None, foreign_key="users.id", index=hash)
    lego_evo_second: Optional[int] = Field(default=None, foreign_key="users.id", index=hash)
    progress: Optional[int] = Field(default=0)
    environment_name: Optional[str] = Field(default=None)
    is_deleted: Optional[bool] = Field(default=0, index=hash)
    is_archived: Optional[bool] = Field(default=0, index=hash)

    area_of_science: Optional[int] = Field(default=None, foreign_key="experiment_areaofscience.id")
    area_of_science_name: Optional["Experiment_AreaOfScience__Base"] = Relationship(
        back_populates="experiments"
    )

    # cloud_provider_requested_name: Optional["Cloud_Provider__Base"] = Relationship(
    #     back_populates="experiments_requested",
    #     sa_relationship=(sa_relationship(foreign_keys="cloud_providers.id")),
    # )
    # cloud_provider_actual_name: Optional["Cloud_Provider__Base"] = Relationship(
    #     back_populates="experiments_actual",
    #     sa_relationship=(sa_relationship(foreign_keys="cloud_providers.id")),
    # )

    department_name: Optional["Department__Base"] = Relationship(back_populates="experiments")
    data_sensivitity_name: Optional["Experiment_DataSensitivity__Base"] = Relationship(
        back_populates="experiments"
    )
    status_name: Optional["Experiment_Status__Base"] = Relationship(
        back_populates="experiments"
    )

    async def __admin_repr__(self, _):
        return f"{self.name} (SPIR-{self.id:04d})"

    async def __admin_select2_repr__(self, _) -> str:
        from html import escape

        return f"<div><span>{escape(f"SPIR-{self.name} (SPIR-{self.id:04d})")}</span></div>"


class Experiment(SQLModel):
    id: Optional[int]
    name: str
    status: Optional[int]
    created_at: datetime.datetime
    updated_at: datetime.datetime
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
    lego_evo_lead: Optional[int]
    lego_evo_second: Optional[int]
    # last_updated: Optional[timestamp]
    progress: Optional[int]
    environment_name: Optional[str]
    is_archived: Optional[bool]


class Experiment__Edit(SQLModel):
    name: str
    status: Optional[int] = Field(default=None)
    delegated: Optional[bool] = Field(default=False)
    department: Optional[int] = Field(default=None)
    research_initiative: Optional[int] = Field(default=None)
    area_of_science: Optional[int] = Field(default=None)
    level_of_effort: Optional[int] = Field(default=None)
    funding_source: Optional[int] = Field(default=None)
    data_sensivitity: Optional[int] = Field(default=None)
    cloud_provider_requested: Optional[int] = Field(default=None)
    cloud_provider_actual: Optional[int] = Field(default=None)
    background: Optional[str] = Field(default="")
    description: Optional[str] = Field(default="")
    goals: Optional[str] = Field(default="")
    fin_forecasted: Optional[float] = Field(default=0.0)
    fin_initial: Optional[float] = Field(default=0.0)
    fin_actual: Optional[float] = Field(default=0.0)
    fin_automated_reports: Optional[bool] = Field(default=False)
    lego_evo_lead: Optional[int] = Field(default=None)
    lego_evo_second: Optional[int] = Field(default=None)
    environment_name: Optional[str] = Field(default="")
    progress: Optional[int] = Field(default=0)


class Experiment_CloudGroupMember(SQLModel):
    FirstName: str
    LastName: str
    DisplayName: str
    Email: str
    UPN: str
    AccountEnabled: bool
    InvitationState: str


class Experiment_CloudGroup(SQLModel):
    GroupName: str
    GroupID: str
    GroupRole: str
    Members: list[Experiment_CloudGroupMember]
