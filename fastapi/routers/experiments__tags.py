from fastapi import APIRouter, HTTPException, Query, Response, status
from sqlmodel import Session, select, delete, or_, and_
from sqlalchemy import exc

from db import engine
from db.models.experiments import *
from db.models import (
    Link__Experiments_Tags,
    Experiment_Tags,
    Experiment_Tags__Base,
)

router = APIRouter(
    prefix="/experiments",
    tags=["Experiments"],
)


@router.get(
    "/{experiment_id}/tags",
    response_model=list[Experiment_Tags],
    responses={404: {"description": "Not found"}},
)
def list_experiment_tags(experiment_id: int):
    with Session(engine) as db:
        experiment = db.get(Experiments__Base, experiment_id)
        if not experiment or experiment.is_deleted:
            raise HTTPException(status_code=404)

        tags = (
            select(Link__Experiments_Tags)
            .where(Link__Experiments_Tags.experiment_id == experiment_id)
            .subquery("tags")
        )
        print(tags)

        rows = (
            select(Experiment_Tags__Base)
            .where(Experiment_Tags__Base.is_deleted == 0)
            .join(tags, Experiment_Tags__Base.id == tags.c.tag_id)
        )

        return db.exec(rows).all()


@router.patch(
    "/{experiment_id}/tags/{tag_id}",
    response_model=Link__Experiments_Tags,
    responses={404: {"description": "Not found"}},
)
def tag_experiment(experiment_id: int, tag_id: int):
    with Session(engine) as db:
        experiment = db.get(Experiments__Base, experiment_id)
        if not experiment or experiment.is_deleted:
            raise HTTPException(status_code=404)

        tag = db.get(Experiment_Tags__Base, tag_id)
        if not tag or tag.is_deleted:
            raise HTTPException(status_code=400, detail="invalid tag")

        row = Link__Experiments_Tags()
        row.experiment_id = experiment_id
        row.tag_id = tag_id
        db.add(row)
        db.commit()
        db.refresh(row)
        return row
