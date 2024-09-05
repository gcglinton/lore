from fastapi import APIRouter, HTTPException, Query, Response, status
from sqlmodel import Session, select, delete, or_, and_, alias, col
from sqlalchemy import exc

from db import engine
from db.models.experiments import *

router = APIRouter(
    prefix="/experiments",
    tags=["Experiments"],
)


def validate_foreign_keys(data):

    from db.models import (
        Department__Base,
        Cloud_Provider__Base,
        Experiment_AreaOfScience__Base,
        Experiment_DataSensitivity__Base,
        Experiment_FundingSource__Base,
        Experiment_LevelOfEffort__Base,
        Experiment_Status__Base,
        User__Base,
    )

    with Session(engine) as db:
        if data.department:
            department = db.get(Department__Base, data.department)
            if data.department and not department:
                raise HTTPException(status_code=400, detail="invalid department")

        # created_user = db.get(Users__Base, data.created_user)
        # if not created_user:
        #     raise HTTPException(status_code=400, detail="invalid user")

        if data.cloud_provider_requested:
            cloud_provider_requested = db.get(Cloud_Provider__Base, data.cloud_provider_requested)
            if data.cloud_provider_requested and not cloud_provider_requested:
                raise HTTPException(status_code=400, detail="invalid cloud provider")

        if data.cloud_provider_actual:
            cloud_provider_actual = db.get(Cloud_Provider__Base, data.cloud_provider_actual)
            if not cloud_provider_actual:
                raise HTTPException(status_code=400, detail="invalid cloud provider")

        if data.status:
            status = db.get(Experiment_Status__Base, data.status)
            if not status:
                raise HTTPException(status_code=400, detail="invalid status")

        if data.area_of_science:
            area_of_science = db.get(Experiment_AreaOfScience__Base, data.area_of_science)
            if not area_of_science:
                raise HTTPException(status_code=400, detail="invalid area of science")

        if data.level_of_effort:
            level_of_effort = db.get(Experiment_LevelOfEffort__Base, data.level_of_effort)
            if not level_of_effort:
                raise HTTPException(status_code=400, detail="invalid level of effort")

        if data.funding_source:
            funding_source = db.get(Experiment_FundingSource__Base, data.funding_source)
            if not funding_source:
                raise HTTPException(status_code=400, detail="invalid funding source")

        if data.data_sensivitity:
            data_sensivitity = db.get(Experiment_DataSensitivity__Base, data.data_sensivitity)
            if not data_sensivitity:
                raise HTTPException(status_code=400, detail="invalid data sensitivity")


@router.get(
    "/",
    response_model=list[Experiment],
)
def list_experiments(
    offset: int = 0,
    limit: int = Query(default=100, le=100),
    status: list[int] = Query(default=[]),
    evo_lead: int = None,
    evo_second: int = None,
    cloud_provider: list[int] = Query(default=[]),
    department: list[int] = Query(default=[]),
):
    with Session(engine) as db:
        statement = select(Experiment__Base).where(
            and_(
                Experiment__Base.is_deleted == 0,
                # col(Experiment__Base.status).in_(status),
                # Experiment__Base.lego_evo_lead == evo_lead,
                # Experiment__Base.lego_evo_second == evo_second,
                # col(Experiment__Base.cloud_provider_actual).in_(cloud_provider),
                # col(Experiment__Base.department).in_(department),
            )
        )

        filters = []
        if status:
            filters.append(col(Experiment__Base.status).in_(status))

        if evo_lead:
            filters.append(Experiment__Base.lego_evo_lead == evo_lead)

        if evo_second:
            filters.append(Experiment__Base.lego_evo_second == evo_second)

        if cloud_provider:
            filters.append(col(Experiment__Base.cloud_provider_actual).in_(cloud_provider))

        if department:
            filters.append(col(Experiment__Base.department).in_(department))

        print(filters)
        # if status:
        #     statement.where(col(Experiment__Base.status).in_(status))

        # if evo_lead:
        #     statement.where(Experiment__Base.lego_evo_lead == evo_lead)

        # if evo_second:
        #     statement.where(Experiment__Base.lego_evo_second == evo_second)

        # if cloud_provider:
        #     statement.where(col(Experiment__Base.cloud_provider_actual).in_(cloud_provider))

        # if department:
        #     statement.where(col(Experiment__Base.department).in_(department))
        if filters:
            statement = statement.where(and_(*filters))
        statement = statement.offset(offset).limit(limit)
        print(statement)
        return db.exec(statement).all()


@router.post(
    "/",
    response_model=Experiment,
)
def add_experiment(body_data: Experiment__Edit, response: Response):
    with Session(engine) as db:
        new_data = Experiment__Base()
        for attribute, value in body_data.__dict__.items():
            setattr(new_data, attribute, value)

        validate_foreign_keys(body_data)

        db.add(new_data)
        db.commit()
        db.refresh(new_data)

        response.status_code = status.HTTP_201_CREATED
        return new_data


@router.get("/{experiment_id}")
def get_an_experiment(experiment_id: int):
    with Session(engine) as db:

        dbrow = db.get(Experiment__Base, experiment_id)
        if not dbrow or dbrow.is_deleted:
            raise HTTPException(status_code=404)

        # return dbrow

        from sqlalchemy import text

        from db.models import Experiment_AreaOfScience__Base, Department__Base

        bigassquery = (
            select(
                Experiment__Base,
                col(Experiment_AreaOfScience__Base.name).label("area_of_science_name"),
                col(Department__Base.name).label("department_name"),
            )
            .join(Experiment_AreaOfScience__Base)
            .join(Department__Base)
            .where(
                Experiment__Base.id == experiment_id,
            )
        )

        bigassquery_result = db.exec(bigassquery).all()
        print(bigassquery_result)

        # experiments.area_of_science, experiment_areaofscience.name AS area_of_science_name,
        # experiments.cloud_provider_actual, cp_actual.name_short AS cloud_provider_actual_name,
        # experiments.cloud_provider_requested, cp_requested.name_short AS cloud_provider_requested_name,
        # experiments.data_sensivitity, experiment_datasensitivity.name AS data_sensivitity_name,
        # experiments.department, departments.name AS department_name,
        # experiments.funding_source, experiment_fundingsource.name AS funding_source_name,
        # experiments.status, experiment_statuses.name AS status_name,
        # experiments.lego_evo_lead, CONCAT(users_evo_lead.name_first, " ", users_evo_lead.name_last) AS lego_evo_lead_name,
        # experiments.lego_evo_second, CONCAT(users_evo_second.name_first, " ", users_evo_second.name_last) AS lego_evo_second_name,
        # experiments.level_of_effort, experiment_levelofeffort.name AS level_of_effort_name
        sql = text(
            """
            SELECT experiments.*, 
                experiment_areaofscience.name AS area_of_science_name,
                cp_actual.name_short AS cloud_provider_actual_name,
                cp_requested.name_short AS cloud_provider_requested_name,
                experiment_datasensitivity.name AS data_sensivitity_name,
                departments.name AS department_name,
                experiment_fundingsource.name AS funding_source_name,
                experiment_statuses.name AS status_name,
                CONCAT(users_evo_lead.name_first, " ", users_evo_lead.name_last) AS lego_evo_lead_name,
                CONCAT(users_evo_second.name_first, " ", users_evo_second.name_last) AS lego_evo_second_name,
                experiment_levelofeffort.name AS level_of_effort_name

            FROM experiments
            LEFT JOIN experiment_areaofscience ON experiments.area_of_science == experiment_areaofscience.id
            LEFT JOIN cloud_providers AS cp_actual ON experiments.cloud_provider_actual == cp_actual.id
            LEFT JOIN cloud_providers AS cp_requested ON experiments.cloud_provider_requested == cp_requested.id
            LEFT JOIN experiment_datasensitivity ON experiments.data_sensivitity == experiment_datasensitivity.id
            LEFT JOIN departments ON experiments.department == departments.id
            LEFT JOIN experiment_fundingsource ON experiments.funding_source == experiment_fundingsource.id
            LEFT JOIN experiment_statuses ON experiments.status == experiment_statuses.id
            LEFT JOIN users AS users_evo_lead ON experiments.lego_evo_lead == users_evo_lead.id
            LEFT JOIN users AS users_evo_second ON experiments.lego_evo_second == users_evo_second.id
            LEFT JOIN experiment_levelofeffort ON experiments.level_of_effort == experiment_levelofeffort.id


            WHERE experiments.id == :experiment_id;
            """
        )
        # ret = db.exec(sql, params={"experiment_id": experiment_id})
        res = db.exec(sql, params={"experiment_id": experiment_id})

        ret = []
        for n in res.all():
            print(n)

            ret = n
        return n


@router.patch(
    "/{experiment_id}/archive",
    response_model=Experiment,
    responses={404: {"description": "Not found"}},
)
def archive_experiment(experiment_id: int):
    with Session(engine) as db:
        row = db.get(Experiment__Base, experiment_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        row.is_archived = 1
        db.add(row)
        db.commit()
        db.refresh(row)
        return row


@router.post(
    "/{experiment_id}",
    response_model=Experiment,
    responses={404: {"description": "Not found"}},
)
def update_experiment(experiment_id: int, body_data: Experiment__Edit):
    with Session(engine) as db:
        row = db.get(Experiment__Base, experiment_id)
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
    responses={404: {"description": "Not found"}},
    status_code=204,
)
def delete_experiment(experiment_id: int):
    with Session(engine) as db:
        row = db.get(Experiment__Base, experiment_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        row.is_deleted = 1
        db.add(row)
        db.commit()
