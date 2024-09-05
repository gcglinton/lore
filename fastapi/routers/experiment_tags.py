from fastapi import APIRouter, HTTPException, Query, Response, status
from sqlmodel import Session, select

from db import engine
from db.models.experiment_tags import *

router = APIRouter(
    prefix="/meta/experiment/tags",
    tags=["Experiment - Tags"],
)


@router.get("/", response_model=list[Experiment_Tag])
def list_experiment_tags(offset: int = 0, limit: int = Query(default=100, le=100)):
    with Session(engine) as db:
        statement = select(Experiment_Tag__Base).where(Experiment_Tag__Base.is_deleted == 0).offset(offset).limit(limit)
        return db.exec(statement).all()


@router.get(
    "/{tag_id}",
    response_model=Experiment_Tag,
    responses={404: {"description": "Not found"}},
)
def get_one_experiment_tag(tag_id: int):
    with Session(engine) as db:
        row = db.get(Experiment_Tag__Base, tag_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        return row


@router.post("/", response_model=Experiment_Tag, status_code=201)
def add_experiment_tag(body_data: Experiment_Tag__Edit, response: Response):
    with Session(engine) as db:
        new_data = Experiment_Tag__Base()
        for attribute, value in body_data.__dict__.items():
            setattr(new_data, attribute, value)
        db.add(new_data)
        db.commit()
        db.refresh(new_data)

        response.status_code = status.HTTP_201_CREATED
        return new_data


@router.put(
    "/{tag_id}",
    response_model=Experiment_Tag,
    responses={404: {"description": "Not found"}},
)
def update_experiment_tag(tag_id: int, body_data: Experiment_Tag__Edit):
    with Session(engine) as db:
        row = db.get(Experiment_Tag__Base, tag_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        body_data_dump = body_data.model_dump(exclude_unset=True)
        row.sqlmodel_update(body_data_dump)
        db.add(row)
        db.commit()
        db.refresh(row)
        return row


@router.delete(
    "/{tag_id}",
    responses={404: {"description": "Not found"}},
    status_code=204,
)
def delete_experiment_tag(tag_id: int):
    with Session(engine) as db:
        row = db.get(Experiment_Tag__Base, tag_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        row.is_deleted = 1
        db.add(row)
        db.commit()
        db.refresh(row)
