import datetime
import uuid
from typing import Optional

from sqlmodel import TEXT, Column, Field, SQLModel


class Lessons_Learned__Base(SQLModel, table=True):
    __tablename__ = "lessons_learned"
    id: Optional[int] = Field(default=None, primary_key=True)
    guid: uuid.UUID
    experiment_id: int = Field(foreign_key="experiments.id")
    user_id: int = Field(foreign_key="users.id")
    sent: datetime.datetime = Field(
        default_factory=datetime.datetime.utcnow,
    )
    submitted: Optional[datetime.datetime] = None
    reason_other: Optional[str] = None
    service_quality: Optional[int] = None
    responsiveness: Optional[int] = None
    reliability: Optional[int] = None
    ease_of_use: Optional[int] = None
    benefits: str = Field(sa_column=Column(TEXT))
    suggestions: str = Field(sa_column=Column(TEXT))
    challenges: str = Field(sa_column=Column(TEXT))
    how_evo_beneficial: str = Field(sa_column=Column(TEXT))
    likely_to_reccommend: Optional[int] = None
    is_deleted: Optional[bool] = Field(default=0, index=hash)


class Lessons_Learned(SQLModel):
    id: int
    guid: uuid.UUID
    experiment_id: int
    user_id: int
    sent: datetime.datetime
    submitted: datetime.datetime
    reason_other: str
    service_quality: int
    responsiveness: int
    reliability: int
    ease_of_use: int
    benefits: str
    suggestions: str
    challenges: str
    how_evo_beneficial: str
    likely_to_reccommend: int


class Lessons_Learned__Send(SQLModel):
    experiment_id: int
    users: list[int]


class Lessons_Learned__Sent(SQLModel):
    experiment_id: int
    user_id: int
    user_email: str
    guid: uuid.UUID
    sent: datetime.datetime


class Lessons_Learned__Submit(SQLModel):
    reason_other: str
    service_quality: int
    responsiveness: int
    reliability: int
    ease_of_use: int
    benefits: str
    suggestions: str
    challenges: str
    how_evo_beneficial: str
    likely_to_reccommend: int
