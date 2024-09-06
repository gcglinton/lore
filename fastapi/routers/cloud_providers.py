from sqlmodel import Session, select
from fastapi import APIRouter, HTTPException, Query, Response, status

from db import engine
from db.models.cloud_providers import Cloud_Provider, Cloud_Provider__Base, Cloud_Provider__Edit

router = APIRouter(
    prefix="/cloud_providers",
    tags=["Cloud Providers"],
)


@router.get(
    "/",
    response_model=list[Cloud_Provider],
)
def list_cloud_providers(offset: int = 0, limit: int = Query(default=100, le=100)):
    with Session(engine) as db:
        statement = (
            select(Cloud_Provider__Base)
            .where(Cloud_Provider__Base.is_deleted == 0)
            .offset(offset)
            .limit(limit)
        )
        return db.exec(statement).all()


@router.get(
    "/{cloudprovider_id}",
    response_model=Cloud_Provider,
    responses={404: {"description": "Not found"}},
)
def get_one_cloud_provider(cloudprovider_id: int):
    with Session(engine) as db:
        row = db.get(Cloud_Provider__Base, cloudprovider_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        return row


@router.post("/", response_model=Cloud_Provider, status_code=201)
def add_cloud_provider(body_data: Cloud_Provider__Edit, response: Response):
    with Session(engine) as db:
        new_data = Cloud_Provider__Base()
        for attribute, value in body_data.__dict__.items():
            setattr(new_data, attribute, value)
        db.add(new_data)
        db.commit()
        db.refresh(new_data)

        response.status_code = status.HTTP_201_CREATED
        return new_data


@router.post(
    "/{cloudprovider_id}",
    response_model=Cloud_Provider,
    responses={404: {"description": "Not found"}},
)
def update_cloud_provider(cloudprovider_id: int, body_data: Cloud_Provider__Edit):
    with Session(engine) as db:
        row = db.get(Cloud_Provider__Base, cloudprovider_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        body_data_dump = body_data.model_dump(exclude_unset=True)
        row.sqlmodel_update(body_data_dump)
        db.add(row)
        db.commit()
        db.refresh(row)
        return row


@router.delete(
    "/{cloudprovider_id}",
    responses={404: {"description": "Not found"}},
    status_code=204,
)
def delete_cloud_provider(cloudprovider_id: int):
    with Session(engine) as db:
        row = db.get(Cloud_Provider__Base, cloudprovider_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        row.is_deleted = 1
        db.add(row)
        db.commit()
        db.refresh(row)
