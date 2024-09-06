from typing import TYPE_CHECKING, Optional

from sqlmodel import SQLModel, Field, Relationship
from sqlmodel import Column, TEXT

from sqlalchemy.orm import relationship as sa_relationship

class Cloud_Provider__Base(SQLModel, table=True):
    __tablename__ = "cloud_providers"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    name_short: str
    contact_name: Optional[str]
    contact_email: Optional[str]
    contact_phone: Optional[str]
    description: Optional[str] = Field(sa_column=Column(TEXT))
    is_deleted: Optional[bool] = Field(default=0, index=hash)

    # experiments_requested: list["Experiment__Base"] = (
    #     Relationship(back_populates="cloud_provider_requested_name",
    #     sa_relationship=(sa_relationship(foreign_keys="experiments.id")), )
    # )
    # experiments_actual: list["Experiment__Base"] = (
    #     Relationship(back_populates="cloud_provider_actual_name",
    #     sa_relationship=(sa_relationship(foreign_keys="experiments.id")),)
    # )


    async def __admin_repr__(self, _):
        return f"{self.name_short}"

    async def __admin_select2_repr__(self, _) -> str:
        from html import escape

        return f"<div><span>{escape(f"{self.name} ({self.name_short})")}</span></div>"


class Cloud_Provider(SQLModel):
    id: int
    name: str
    name_short: str
    contact_name: str
    contact_email: str
    contact_phone: str
    description: str


class Cloud_Provider__Edit(SQLModel):
    name: str
    name_short: str
    contact_name: Optional[str]
    contact_email: Optional[str]
    contact_phone: Optional[str]
    description: Optional[str]
