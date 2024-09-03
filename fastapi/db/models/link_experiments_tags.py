from sqlmodel import Field, SQLModel


class Link__Experiments_Tags(SQLModel, table=True):
    __tablename__ = "link_experiments_tags"
    experiment_id: int = Field(foreign_key="experiments.id", primary_key=True)
    tag_id: int = Field(foreign_key="experiment_tags.id", primary_key=True)
