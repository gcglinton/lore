from fastapi import FastAPI

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
from admin import admin

app = FastAPI()

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

# Mount admin to your app
admin.mount_to(app)
