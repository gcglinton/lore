from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select

from db import engine
from db.models.experiment_datasensitivity import *

router = APIRouter(
    prefix="/meta/experiment/datasensitivity",
    tags=["Experiment -  Data Sensitivity"],
)


@router.get("/", response_model=list[Experiment_DataSensitivity])
def list_experiment_data_sensivitity():
    with Session(engine) as db:
        statement = select(Experiment_DataSensitivity__Base).where(
            Experiment_DataSensitivity__Base.is_deleted == 0
        )
        return db.exec(statement).all()


@router.post("/", response_model=Experiment_DataSensitivity)
def add_experiment_data_sensivitity(datasensitivity: Experiment_DataSensitivity__Edit):
    with Session(engine) as db:
        new_data = Experiment_DataSensitivity__Base()
        for attribute, value in datasensitivity.__dict__.items():
            setattr(new_data, attribute, value)
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data


@router.put("/{datasensitivity_id}", response_model=Experiment_DataSensitivity)
def update_experiment_data_sensivitity(
    datasensitivity_id: int, datasensitivity: Experiment_DataSensitivity__Edit
):
    with Session(engine) as db:
        row = db.get(Experiment_DataSensitivity__Base, datasensitivity_id)
        if not row or row.is_deleted:
            raise HTTPException(datasensitivity_code=404)
        datasensitivity_data = datasensitivity.model_dump(exclude_unset=True)
        row.sqlmodel_update(datasensitivity_data)
        db.add(row)
        db.commit()
        db.refresh(row)
        return row


@router.delete("/{datasensitivity_id}", response_model=Experiment_DataSensitivity)
def delete_experiment_(datasensitivity_id: int):
    with Session(engine) as db:
        row = db.get(Experiment_DataSensitivity__Base, datasensitivity_id)
        if not row or row.is_deleted:
            raise HTTPException(datasensitivity_code=404)
        row.is_deleted = 1
        db.add(row)
        db.commit()
        db.refresh(row)
        return row
