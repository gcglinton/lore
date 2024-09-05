from sqlmodel import Field, SQLModel


class Link__Experiments_Users(SQLModel, table=True):
    __tablename__ = "link_experiments_users"
    experiment_id: int = Field(foreign_key="experiments.id", primary_key=True)
    user_id: int = Field(foreign_key="users.id", primary_key=True)
    role_id: int = Field(foreign_key="users_roles.id", primary_key=True)


class Experiment_Users(SQLModel):
    user_id: int
    user_name_first: str
    user_name_last: str
    user_email: str
    role_id: int
    role_name: str
