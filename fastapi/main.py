from fastapi import FastAPI

app = FastAPI()

from db import engine

from routers import cloud_providers
from routers import departments
from routers import experiment_areaofscience
from routers import experiment_datasensitivity
from routers import experiment_fundingsource
from routers import experiment_levelofeffort
from routers import experiment_status
from routers import experiment_tags
from routers import experiments
from routers import experiments__related
from routers import experiments__tags
from routers import experiments__users
from routers import users_roles
from routers import users

app.include_router(cloud_providers.router)
app.include_router(departments.router)
app.include_router(experiment_areaofscience.router)
app.include_router(experiment_datasensitivity.router)
app.include_router(experiment_fundingsource.router)
app.include_router(experiment_levelofeffort.router)
app.include_router(experiment_status.router)
app.include_router(experiment_tags.router)
app.include_router(experiments.router)
app.include_router(experiments__related.router)
app.include_router(experiments__tags.router)
app.include_router(experiments__users.router)
app.include_router(users.router)
app.include_router(users_roles.router)


# -----------------------------------------------------------
#                        ADMIN
# -----------------------------------------------------------

# from starlette.applications import Starlette
from starlette_admin.contrib.sqla import Admin, ModelView

admin = Admin(engine, title="LORE")

from db.models import Experiment_AreaOfScience__Base

admin.add_view(
    ModelView(
        Experiment_AreaOfScience__Base,
        label="Experiments - Areas of Science",
        name="Area of Science",
    )
)

from db.models import Experiment_DataSensitivity__Base

admin.add_view(
    ModelView(
        Experiment_DataSensitivity__Base,
        label="Experiments - Data Sensitivities",
        name="Data Sensitivity",
    )
)

from db.models import Experiment_FundingSource__Base

admin.add_view(
    ModelView(
        Experiment_FundingSource__Base,
        label="Experiments - Funding Sources",
        name="Funding Source",
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

from db.models import Cloud_Providers__Base

admin.add_view(
    ModelView(Cloud_Providers__Base, label="Cloud Providers", name="Cloud Provider")
)

from db.models import Experiments__Base

admin.add_view(ModelView(Experiments__Base, label="Experiments", name="Exoeriment"))

from db.models import Departments__Base

admin.add_view(ModelView(Departments__Base, label="Departments", name="Department"))

from db.models import Users__Base

admin.add_view(ModelView(Users__Base, label="Users", name="User"))

from db.models import Users_Roles__Base

admin.add_view(ModelView(Users_Roles__Base, label="Users - Roles", name="Role"))

# Mount admin to your app
admin.mount_to(app)
