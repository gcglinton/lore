from fastapi import APIRouter, HTTPException, Query
from sqlmodel import Session, select

from db import engine
from db.models.experiment_areaofscience import *

router = APIRouter(
    prefix="/meta/experiment/areaofscience",
    tags=["Experiment - Area of Science"],
)


@router.get("/", response_model=list[Experiment_AreaOfScience])
def list_experiment_areas_of_science(
    offset: int = 0, limit: int = Query(default=100, le=100)
):
    with Session(engine) as db:
        statement = (
            select(Experiment_AreaOfScience__Base)
            .where(Experiment_AreaOfScience__Base.is_deleted == 0)
            .offset(offset)
            .limit(limit)
        )
        return db.exec(statement).all()


@router.get(
    "/{areaofscience_id}",
    response_model=Experiment_AreaOfScience,
)
def get_one_experiment_area_of_science(areaofscience_id: int):
    with Session(engine) as db:
        row = db.get(Experiment_AreaOfScience__Base, areaofscience_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        return row


@router.post("/", response_model=Experiment_AreaOfScience)
def add_experiment_area_of_science(body_data: Experiment_AreaOfScience__Edit):
    with Session(engine) as db:
        new_data = Experiment_AreaOfScience__Base()
        for attribute, value in body_data.__dict__.items():
            setattr(new_data, attribute, value)
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data


@router.put("/{areaofscience_id}", response_model=Experiment_AreaOfScience)
def update_experiment_area_of_science(
    item_id: int, body_data: Experiment_AreaOfScience__Edit
):
    with Session(engine) as db:
        row = db.get(Experiment_AreaOfScience__Base, item_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        body_data_dump = body_data.model_dump(exclude_unset=True)
        row.sqlmodel_update(body_data_dump)
        db.add(row)
        db.commit()
        db.refresh(row)
        return row


@router.delete("/{areaofscience_id}", response_model=Experiment_AreaOfScience)
def delete_experiment_area_of_science(item_id: int):
    with Session(engine) as db:
        row = db.get(Experiment_AreaOfScience__Base, item_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        row.is_deleted = 1
        db.add(row)
        db.commit()
        db.refresh(row)
        return row
