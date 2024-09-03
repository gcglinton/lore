from fastapi import APIRouter, HTTPException, Query
from sqlmodel import Session, select

from db import engine
from db.models.experiments import *
from db.models import (
    Link__Experiments_Tags,
    Link__Experiments_Users,
    Link__Experiments_Related,
)


router = APIRouter(
    prefix="/experiments",
    tags=["Experiments"],
)


def validate_foreign_keys(data):

    from db.models import (
        Departments__Base,
        Cloud_Providers__Base,
        Experiment_AreaOfScience__Base,
        Experiment_DataSensitivity__Base,
        Experiment_FundingSource__Base,
        Experiment_LevelOfEffort__Base,
        Experiment_Status__Base,
        Users__Base,
    )

    with Session(engine) as db:
        if data.department:
            department = db.get(Departments__Base, data.department)
            if data.department and not department:
                raise HTTPException(status_code=400, detail="invalid department")

        # created_user = db.get(Users__Base, data.created_user)
        # if not created_user:
        #     raise HTTPException(status_code=400, detail="invalid user")

        if data.cloud_provider_requested:
            cloud_provider_requested = db.get(
                Cloud_Providers__Base, data.cloud_provider_requested
            )
            if data.cloud_provider_requested and not cloud_provider_requested:
                raise HTTPException(status_code=400, detail="invalid cloud provider")

        if data.cloud_provider_actual:
            cloud_provider_actual = db.get(
                Cloud_Providers__Base, data.cloud_provider_actual
            )
            if not cloud_provider_actual:
                raise HTTPException(status_code=400, detail="invalid cloud provider")

        if data.status:
            status = db.get(Experiment_Status__Base, data.status)
            if not status:
                raise HTTPException(status_code=400, detail="invalid status")

        if data.area_of_science:
            area_of_science = db.get(
                Experiment_AreaOfScience__Base, data.area_of_science
            )
            if not area_of_science:
                raise HTTPException(status_code=400, detail="invalid area of science")

        if data.level_of_effort:
            level_of_effort = db.get(
                Experiment_LevelOfEffort__Base, data.level_of_effort
            )
            if not level_of_effort:
                raise HTTPException(status_code=400, detail="invalid level of effort")

        if data.funding_source:
            funding_source = db.get(Experiment_FundingSource__Base, data.funding_source)
            if not funding_source:
                raise HTTPException(status_code=400, detail="invalid funding source")

        if data.data_sensivitity:
            data_sensivitity = db.get(
                Experiment_DataSensitivity__Base, data.data_sensivitity
            )
            if not data_sensivitity:
                raise HTTPException(status_code=400, detail="invalid data sensitivity")


@router.get(
    "/",
    response_model=list[Experiments],
)
def list_experiments(offset: int = 0, limit: int = Query(default=100, le=100)):
    with Session(engine) as db:
        statement = (
            select(Experiments__Base)
            .where(Experiments__Base.is_deleted == 0)
            .offset(offset)
            .limit(limit)
        )
        return db.exec(statement).all()


@router.post(
    "/",
    response_model=Experiments,
)
def add_experiment(body_data: Experiments__Edit):
    with Session(engine) as db:
        new_data = Experiments__Base()
        for attribute, value in body_data.__dict__.items():
            setattr(new_data, attribute, value)

        validate_foreign_keys(body_data)

        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data


@router.get(
    "/{experiment_id}",
    response_model=Experiments,
)
def get_an_experiment(experiment_id: int):
    with Session(engine) as db:
        row = db.get(Experiments__Base, experiment_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        return row


@router.patch(
    "/{experiment_id}/archive",
    response_model=Experiments,
    responses={404: {"description": "Not found"}},
)
def archive_experiment(item_id: int):
    with Session(engine) as db:
        row = db.get(Experiments__Base, item_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        row.is_archived = 1
        db.add(row)
        db.commit()
        db.refresh(row)
        return row


@router.patch(
    "/{experiment_id}/tag/{tag_id}",
    response_model=Link__Experiments_Tags,
    responses={404: {"description": "Not found"}},
)
def tag_experiment(item_id: int, tag_id: int):
    from db.models import Experiment_Tags__Base

    with Session(engine) as db:
        experiment = db.get(Experiments__Base, item_id)
        if not experiment or experiment.is_deleted:
            raise HTTPException(status_code=404)

        tag = db.get(Experiment_Tags__Base, tag_id)
        if not tag or tag.is_deleted:
            raise HTTPException(status_code=400, detail="invalid tag")

        row = Link__Experiments_Tags()
        row.experiment_id = item_id
        row.tag_id = tag_id
        db.add(row)
        db.commit()
        db.refresh(row)
        return row


@router.patch(
    "/{experiment_id}/user/{user_id}/role/{role_id}",
    response_model=Link__Experiments_Tags,
    responses={404: {"description": "Not found"}},
)
def tag_experiment(item_id: int, user_id: int, role_id: int):
    from db.models import Users__Base, Users_Roles__Base

    with Session(engine) as db:
        experiment = db.get(Experiments__Base, item_id)
        if not experiment or experiment.is_deleted:
            raise HTTPException(status_code=404)

        user = db.get(Users__Base, user_id)
        if not user or user.is_deleted:
            raise HTTPException(status_code=400, detail="invalid user")

        role = db.get(Users_Roles__Base, role_id)
        if not role or role.is_deleted:
            raise HTTPException(status_code=400, detail="invalid role")

        row = Link__Experiments_Users()
        row.experiment_id = item_id
        row.user_id = user_id
        row.role_id = role_id
        db.add(row)
        db.commit()
        db.refresh(row)
        return row


@router.patch(
    "/{experiment_id}/related/{related_id}",
    response_model=Link__Experiments_Related,
    responses={404: {"description": "Not found"}},
)
def tag_experiment(item_id: int, related_id: int):
    with Session(engine) as db:
        experiment = db.get(Experiments__Base, item_id)
        if not experiment or experiment.is_deleted:
            raise HTTPException(status_code=404)

        experiment_related = db.get(Experiments__Base, related_id)
        if not experiment_related or experiment_related.is_deleted:
            raise HTTPException(status_code=404)

        row = Link__Experiments_Related
        row.experiment_1 = item_id
        row.experiment_2 = related_id
        db.add(row)
        db.commit()
        db.refresh(row)

        return row


@router.post(
    "/{experiment_id}",
    response_model=Experiments,
    responses={404: {"description": "Not found"}},
)
def update_update(item_id: int, body_data: Experiments__Edit):
    with Session(engine) as db:
        row = db.get(Experiments__Base, item_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)

        validate_foreign_keys(body_data)

        body_data_dump = body_data.model_dump(exclude_unset=True)
        row.sqlmodel_update(body_data_dump)
        db.add(row)
        db.commit()
        db.refresh(row)
        return row


@router.delete(
    "/{experiment_id}",
    response_model=Experiments,
    responses={404: {"description": "Not found"}},
)
def delete_experiment(item_id: int):
    with Session(engine) as db:
        row = db.get(Experiments__Base, item_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        row.is_deleted = 1
        db.add(row)
        db.commit()
        db.refresh(row)
        return row
