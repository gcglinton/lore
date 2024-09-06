# -----------------------------------------------------------
#                        ADMIN
# -----------------------------------------------------------

# from starlette.applications import Starlette
from starlette_admin.contrib.sqla import Admin, ModelView

from db import engine

from db.models import Experiment_AreaOfScience__Base, Experiment_DataSensitivity__Base
from db.models import Experiment_FundingSource__Base, Experiment_LevelOfEffort__Base
from db.models import Experiment_Status__Base, Experiment_Tag__Base
from db.models import Cloud_Provider__Base, Experiment__Base
from db.models import Department__Base, User__Base
from db.models import User_Role__Base

admin = Admin(engine, title="LORE")
admin.add_view(
    ModelView(
        Experiment_AreaOfScience__Base,
        label="Experiments - Areas of Science",
        name="Area of Science",
    )
)

admin.add_view(
    ModelView(
        Experiment_DataSensitivity__Base,
        label="Experiments - Data Sensitivities",
        name="Data Sensitivity",
    )
)

admin.add_view(
    ModelView(
        Experiment_FundingSource__Base,
        label="Experiments - Funding Sources",
        name="Funding Source",
    )
)

admin.add_view(
    ModelView(
        Experiment_LevelOfEffort__Base,
        label="Experiments - Levels Of Effort",
        name="Level Of Effort",
    )
)

admin.add_view(ModelView(Experiment_Status__Base, label="Experiments - Statuses", name="Status"))

admin.add_view(ModelView(Experiment_Tag__Base, label="Experiments - Tags", name="Tag"))

admin.add_view(ModelView(Cloud_Provider__Base, label="Cloud Providers", name="Cloud Provider"))

admin.add_view(ModelView(Experiment__Base, label="Experiments", name="Exoeriment"))

admin.add_view(ModelView(Department__Base, label="Departments", name="Department"))

admin.add_view(ModelView(User__Base, label="Users", name="User"))

admin.add_view(ModelView(User_Role__Base, label="Users - Roles", name="Role"))
