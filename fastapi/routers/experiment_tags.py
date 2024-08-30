from fastapi import APIRouter, HTTPException


from sqlmodel import Session, select
from model import engine


router = APIRouter(
    prefix = "/meta/experiment/tags",
    tags = ["Experiment - Tags"],
    )

from model import Experiment_Tags, Experiment_Tags__Base, Experiment_Tags__Edit

@router.get("/", response_model=list[Experiment_Tags])
def list_experiment_tags():
    with Session(engine) as db:
        statement = select(Experiment_Tags__Base).where(Experiment_Tags__Base.is_deleted == 0)
        return db.exec(statement).all()
    
@router.post("/", response_model=Experiment_Tags)
def add_experiment_tag(tag: Experiment_Tags__Edit):
    with Session(engine) as db:
        new_data = Experiment_Tags__Base()
        for attribute, value in tag.__dict__.items():
            setattr(new_data, attribute, value)
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data

@router.put(
    "/{tag_id}",
    response_model=Experiment_Tags,
    responses={404: {"description": "Not found"}},
)
def update_experiment_tag(tag_id: int, tag: Experiment_Tags__Edit):
    with Session(engine) as db:
        row = db.get(Experiment_Tags__Base, tag_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        tag_data = tag.model_dump(exclude_unset=True)
        row.sqlmodel_update(tag_data)
        db.add(row)
        db.commit()
        db.refresh(row)
        return row

@router.delete(
    "/{tag_id}",
    response_model=Experiment_Tags,
    responses={404: {"description": "Not found"}},
)
def delete_experiment_tag(tag_id: int):
    with Session(engine) as db:
        row = db.get(Experiment_Tags__Base, tag_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        row.is_deleted = 1
        db.add(row)
        db.commit()
        db.refresh(row)
        return row