from fastapi import APIRouter, HTTPException

from sqlmodel import Session, select
from model import engine


router = APIRouter(
    prefix = "/meta/experiment/status",
    tags = ["Experiment - Status"],
    )

from model import Experiment_Status__Base, Experiment_Status, Experiment_Status__Edit

@router.get("/", response_model=list[Experiment_Status])
def list_experiment_statuses():
    with Session(engine) as db:
        statement = select(Experiment_Status__Base).where(Experiment_Status__Base.is_deleted == 0)
        return db.exec(statement).all()
    
@router.post("/", response_model=Experiment_Status)
def add_experiment_status(status: Experiment_Status__Edit):
    with Session(engine) as db:
        new_data = Experiment_Status__Base()
        for attribute, value in status.__dict__.items():
            setattr(new_data, attribute, value)
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data

@router.put("/{status_id}", response_model=Experiment_Status)
def update_experiment_status(status_id: int, status: Experiment_Status__Edit):
    with Session(engine) as db:
        db_status = db.get(Experiment_Status__Base, status_id)
        if not db_status or db_status.is_deleted or db_status.is_archived:
            raise HTTPException(status_code=404)
        status_data = status.model_dump(exclude_unset=True)
        db_status.sqlmodel_update(status_data)
        db.add(db_status)
        db.commit()
        db.refresh(db_status)
        return db_status

@router.delete("/{status_id}", response_model=Experiment_Status)
def delete_experiment_status(status_id: int):
    with Session(engine) as db:
        db_status = db.get(Experiment_Status__Base, status_id)
        if not db_status or db_status.is_deleted:
            raise HTTPException(status_code=404)
        db_status.is_deleted = 1
        db.add(db_status)
        db.commit()
        db.refresh(db_status)
        return db_status