from fastapi import APIRouter, HTTPException, Query, Response, status
from sqlmodel import Session, select

from db import engine
from db.models.departments import *

router = APIRouter(
    prefix="/departments",
    tags=["Departments"],
)


@router.get(
    "/",
    response_model=list[Department],
)
def list_departments(offset: int = 0, limit: int = Query(default=100, le=100)):
    with Session(engine) as db:
        statement = (
            select(Department__Base)
            .where(Department__Base.is_deleted == 0)
            .offset(offset)
            .limit(limit)
        )
        return db.exec(statement).all()


@router.get(
    "/{department_id}",
    response_model=Department,
    responses={404: {"description": "Not found"}},
)
def get_one_department(department_id: int):
    with Session(engine) as db:
        row = db.get(Department__Base, department_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        return row


@router.post("/", response_model=Department, status_code=201)
def add_department(body_data: Department__Edit, response: Response):
    with Session(engine) as db:
        new_data = Department__Base()
        for attribute, value in body_data.__dict__.items():
            setattr(new_data, attribute, value)
        db.add(new_data)
        db.commit()
        db.refresh(new_data)

        response.status_code = status.HTTP_201_CREATED
        return new_data


@router.post(
    "/{department_id}",
    response_model=Department,
    responses={404: {"description": "Not found"}},
)
def update_department(department_id: int, body_data: Department__Edit):
    with Session(engine) as db:
        row = db.get(Department__Base, department_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        body_data_dump = body_data.model_dump(exclude_unset=True)
        row.sqlmodel_update(body_data_dump)
        db.add(row)
        db.commit()
        db.refresh(row)
        return row


@router.delete(
    "/{department_id}",
    responses={404: {"description": "Not found"}},
    status_code=204,
)
def delete_department(department_id: int):
    with Session(engine) as db:
        row = db.get(Department__Base, department_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        row.is_deleted = 1
        db.add(row)
        db.commit()
        db.refresh(row)
