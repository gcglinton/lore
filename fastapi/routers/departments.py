from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select

from db import engine
from db.models.departments import *

router = APIRouter(
    prefix="/departments",
    tags=["Departments"],
)


@router.get(
    "/",
    response_model=list[Departments],
)
def list_departments():
    with Session(engine) as db:
        statement = select(Departments__Base).where(Departments__Base.is_deleted == 0)
        return db.exec(statement).all()


@router.post(
    "/",
    response_model=Departments,
)
def add_department(department: Departments__Edit):
    with Session(engine) as db:
        new_data = Departments__Base()
        for attribute, value in department.__dict__.items():
            setattr(new_data, attribute, value)
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data


@router.post(
    "/{department_id}",
    response_model=Departments,
    responses={404: {"description": "Not found"}},
)
def update_department(department_id: int, department: Departments__Edit):
    with Session(engine) as db:
        row = db.get(Departments__Base, department_id)
        if not row or row.is_deleted:
            raise HTTPException(code=404)
        department_data = department.model_dump(exclude_unset=True)
        row.sqlmodel_update(department_data)
        db.add(row)
        db.commit()
        db.refresh(row)
        return row


@router.delete(
    "/{department_id}",
    response_model=Departments,
    responses={404: {"description": "Not found"}},
)
def delete_department(department_id: int):
    with Session(engine) as db:
        row = db.get(Departments__Base, department_id)
        if not row or row.is_deleted:
            raise HTTPException(code=404)
        row.is_deleted = 1
        db.add(row)
        db.commit()
        db.refresh(row)
        return row
