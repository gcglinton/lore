from fastapi import APIRouter, HTTPException, Query, Response, status
from sqlmodel import Session, select

from db import engine
from db.models.experiment_fundingsource import *

router = APIRouter(
    prefix="/meta/experiment/fundingsource",
    tags=["Experiment - Funding Source"],
)


@router.get("/", response_model=list[Experiment_FundingSource])
def list_experiment_funding_sources(
    offset: int = 0, limit: int = Query(default=100, le=100)
):
    with Session(engine) as db:
        statement = (
            select(Experiment_FundingSource__Base)
            .where(Experiment_FundingSource__Base.is_deleted == 0)
            .offset(offset)
            .limit(limit)
        )
        return db.exec(statement).all()


@router.get(
    "/{fundingsource_id}",
    response_model=Experiment_FundingSource,
    responses={404: {"description": "Not found"}},
)
def get_one_experiment_funding_source(fundingsource_id: int):
    with Session(engine) as db:
        row = db.get(Experiment_FundingSource__Base, fundingsource_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        return row


@router.post("/", response_model=Experiment_FundingSource, status_code=201)
def add_experiment_funding_source(
    posted_data: Experiment_FundingSource__Edit, response: Response
):
    with Session(engine) as db:
        new_data = Experiment_FundingSource__Base()
        for attribute, value in posted_data.__dict__.items():
            setattr(new_data, attribute, value)
        db.add(new_data)
        db.commit()
        db.refresh(new_data)

        response.status_code = status.HTTP_201_CREATED
        return new_data


@router.put("/{fundingsource_id}", response_model=Experiment_FundingSource)
def update_experiment_funding_source(
    fundingsource_id: int, posted_data: Experiment_FundingSource__Edit
):
    with Session(engine) as db:
        row = db.get(Experiment_FundingSource__Base, fundingsource_id)
        if not row or row.is_deleted:
            raise HTTPException(code=404)
        posted_data_dump = posted_data.model_dump(exclude_unset=True)
        row.sqlmodel_update(posted_data_dump)
        db.add(row)
        db.commit()
        db.refresh(row)
        return row


@router.delete(
    "/{fundingsource_id}",
    responses={404: {"description": "Not found"}},
    status_code=204,
)
def delete_experiment_funding_sourcey(fundingsource_id: int):
    with Session(engine) as db:
        row = db.get(Experiment_FundingSource__Base, fundingsource_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        row.is_deleted = 1
        db.add(row)
        db.commit()
        db.refresh(row)
