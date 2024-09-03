from sqlmodel import Field, SQLModel


class Link__Experiments_Related(SQLModel, table=True):
    __tablename__ = "link_experiments_related"
    experiment_1: int = Field(foreign_key="experiments.id", primary_key=True)
    experiment_2: int = Field(foreign_key="experiments.id", primary_key=True)
