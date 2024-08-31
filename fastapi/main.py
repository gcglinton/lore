from fastapi import FastAPI

app = FastAPI()

from db import engine

from routers import experiment_datasensitivity
from routers import experiment_levelofeffort
from routers import experiment_status
from routers import experiment_tags
from routers import users


app.include_router(experiment_datasensitivity.router)
app.include_router(experiment_levelofeffort.router)
app.include_router(experiment_status.router)
app.include_router(experiment_tags.router)
app.include_router(users.router)

# from starlette.applications import Starlette
from starlette_admin.contrib.sqla import Admin, ModelView

admin = Admin(engine, title="LORE")

from db.models import Experiment_DataSensitivity__Base

admin.add_view(
    ModelView(
        Experiment_DataSensitivity__Base,
        label="Experiments - Data Sensitivities",
        name="Data Sensitivity",
    )
)

from db.models import Experiment_LevelOfEffort__Base

admin.add_view(
    ModelView(
        Experiment_LevelOfEffort__Base,
        label="Experiments - Levels Of Effort",
        name="Level Of Effort",
    )
)

from db.models import Experiment_Status__Base

admin.add_view(
    ModelView(Experiment_Status__Base, label="Experiments - Statuses", name="Status")
)

from db.models import Experiment_Tags__Base

admin.add_view(ModelView(Experiment_Tags__Base, label="Experiments - Tags", name="Tag"))

from db.models import Departments__Base

admin.add_view(ModelView(Departments__Base, label="Departments", name="Department"))

from db.models import Users__Base

admin.add_view(ModelView(Users__Base, label="Users", name="User"))

# Mount admin to your app
admin.mount_to(app)
