from admin import admin
from routers import (
    cloud_providers,
    departments,
    experiment_areaofscience,
    experiment_datasensitivity,
    experiment_fundingsource,
    experiment_levelofeffort,
    experiment_status,
    experiment_tags,
    experiments,
    experiments__related,
    experiments__tags,
    experiments__users,
    lessons_learned,
    users,
    users_roles,
)

from fastapi import FastAPI

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
app.include_router(lessons_learned.router)
app.include_router(users.router)
app.include_router(users_roles.router)

# Mount admin to your app
admin.mount_to(app)
