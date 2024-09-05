from fastapi import APIRouter, HTTPException, Query, Response, status
from sqlmodel import Session, select

from db import engine
from db.models.experiment_datasensitivity import *

router = APIRouter(
    prefix="/meta/experiment/datasensitivity",
    tags=["Experiment -  Data Sensitivity"],
)


@router.get("/", response_model=list[Experiment_DataSensitivity])
def list_experiment_data_sensivitities(offset: int = 0, limit: int = Query(default=100, le=100)):
    with Session(engine) as db:
        statement = (
            select(Experiment_DataSensitivity__Base)
            .where(Experiment_DataSensitivity__Base.is_deleted == 0)
            .offset(offset)
            .limit(limit)
        )
        return db.exec(statement).all()


@router.get(
    "/{datasensitivity_id}",
    response_model=Experiment_DataSensitivity,
    responses={404: {"description": "Not found"}},
)
def get_one_experiment_area_of_science(datasensitivity_id: int):
    with Session(engine) as db:
        row = db.get(Experiment_DataSensitivity__Base, datasensitivity_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        return row


@router.post("/", response_model=Experiment_DataSensitivity, status_code=201)
def add_experiment_data_sensivitity(
    posted_data: Experiment_DataSensitivity__Edit, response: Response
):
    with Session(engine) as db:
        new_data = Experiment_DataSensitivity__Base()
        for attribute, value in posted_data.__dict__.items():
            setattr(new_data, attribute, value)
        db.add(new_data)
        db.commit()
        db.refresh(new_data)

        response.status_code = status.HTTP_201_CREATED
        return new_data


@router.put("/{datasensitivity_id}", response_model=Experiment_DataSensitivity)
def update_experiment_data_sensivitity(
    datasensitivity_id: int, posted_data: Experiment_DataSensitivity__Edit
):
    with Session(engine) as db:
        row = db.get(Experiment_DataSensitivity__Base, datasensitivity_id)
        if not row or row.is_deleted:
            raise HTTPException(code=404)
        posted_data_dump = posted_data.model_dump(exclude_unset=True)
        row.sqlmodel_update(posted_data_dump)
        db.add(row)
        db.commit()
        db.refresh(row)
        return row


@router.delete(
    "/{datasensitivity_id}",
    responses={404: {"description": "Not found"}},
    status_code=204,
)
def delete_experiment_data_sensivitity(datasensitivity_id: int):
    with Session(engine) as db:
        row = db.get(Experiment_DataSensitivity__Base, datasensitivity_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        row.is_deleted = 1
        db.add(row)
        db.commit()
        db.refresh(row)
