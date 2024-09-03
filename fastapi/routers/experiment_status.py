from fastapi import APIRouter, HTTPException, Query
from sqlmodel import Session, select

from db import engine
from db.models.experiment_status import *

router = APIRouter(
    prefix="/meta/experiment/status",
    tags=["Experiment - Status"],
)


@router.get("/", response_model=list[Experiment_Status])
def list_experiment_statuses(offset: int = 0, limit: int = Query(default=100, le=100)):
    with Session(engine) as db:
        statement = (
            select(Experiment_Status__Base)
            .where(Experiment_Status__Base.is_deleted == 0)
            .offset(offset)
            .limit(limit)
        )
        return db.exec(statement).all()


@router.get(
    "/{status_id}",
    response_model=Experiment_Status,
)
def get_one_experiment_status(status_id: int):
    with Session(engine) as db:
        row = db.get(Experiment_Status__Base, status_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        return row


@router.post("/", response_model=Experiment_Status)
def add_experiment_status(body_data: Experiment_Status__Edit):
    with Session(engine) as db:
        new_data = Experiment_Status__Base()
        for attribute, value in body_data.__dict__.items():
            setattr(new_data, attribute, value)
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data


@router.put("/{status_id}", response_model=Experiment_Status)
def update_experiment_status(item_id: int, body_data: Experiment_Status__Edit):
    with Session(engine) as db:
        row = db.get(Experiment_Status__Base, item_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        body_data_dump = body_data.model_dump(exclude_unset=True)
        row.sqlmodel_update(body_data_dump)
        db.add(row)
        db.commit()
        db.refresh(row)
        return row


@router.delete("/{status_id}", response_model=Experiment_Status)
def delete_experiment_status(item_id: int):
    with Session(engine) as db:
        row = db.get(Experiment_Status__Base, item_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        row.is_deleted = 1
        db.add(row)
        db.commit()
        db.refresh(row)
        return row
