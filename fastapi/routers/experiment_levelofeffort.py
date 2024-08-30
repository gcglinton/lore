from fastapi import APIRouter, HTTPException

from sqlmodel import Session, select
from model import engine


router = APIRouter(
    prefix = "/meta/experiment/levelofeffort",
    tags = ["Experiment - Level Of Effort"],
    )

from model import Experiment_LevelOfEffort, Experiment_LevelOfEffort__Base, Experiment_LevelOfEffort__Edit

@router.get("/", response_model=list[Experiment_LevelOfEffort])
def list_experiment_level_of_efforts():
    with Session(engine) as db:
        statement = select(Experiment_LevelOfEffort__Base).where(Experiment_LevelOfEffort__Base.is_deleted == 0)
        return db.exec(statement).all()
    
@router.post("/", response_model=Experiment_LevelOfEffort)
def add_experiment_level_of_effort(levelofeffort: Experiment_LevelOfEffort__Edit):
    with Session(engine) as db:
        new_data = Experiment_LevelOfEffort__Base()
        for attribute, value in levelofeffort.__dict__.items():
            setattr(new_data, attribute, value)
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data

@router.put(
    "/levelofeffort/{levelofeffort_id}", 
    response_model=Experiment_LevelOfEffort,
    responses={404: {"description": "Not found"}},
)
def update_experiment_level_of_effort(levelofeffort_id: int, levelofeffort: Experiment_LevelOfEffort__Edit):
    with Session(engine) as db:
        row = db.get(Experiment_LevelOfEffort__Base, levelofeffort_id)
        if not row or row.is_deleted:
            raise HTTPException(levelofeffort_code=404)
        levelofeffort_data = levelofeffort.model_dump(exclude_unset=True)
        row.sqlmodel_update(levelofeffort_data)
        db.add(row)
        db.commit()
        db.refresh(row)
        return row

@router.delete(
    "/{levelofeffort_id}",
    response_model=Experiment_LevelOfEffort,
    responses={404: {"description": "Not found"}},
)
def delete_experiment_level_of_effort(levelofeffort_id: int):
    with Session(engine) as db:
        row = db.get(Experiment_LevelOfEffort__Base, levelofeffort_id)
        if not row or row.is_deleted:
            raise HTTPException(levelofeffort_code=404)
        row.is_deleted = 1
        db.add(row)
        db.commit()
        db.refresh(row)
        return row