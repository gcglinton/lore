from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select

from db import engine
from db.models.users import *
from db.models.departments import Departments__Base

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/", response_model=list[Users])
def list_users():
    with Session(engine) as db:
        statement = select(Users__Base).where(Users__Base.is_deleted == 0)
        return db.exec(statement).all()


@router.post("/", response_model=Users)
def add_user(body_data: Users__Edit):
    with Session(engine) as db:
        new_data = Users__Base()
        for attribute, value in body_data.__dict__.items():
            setattr(new_data, attribute, value)

        sbda = db.get(Departments__Base, body_data.sbda)
        if not sbda:
            raise HTTPException(status_code=400, detail="invalid sbda")
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data


@router.put(
    "/{user_id}",
    response_model=Users,
    responses={404: {"description": "Not found"}},
)
def update_user(item_id: int, body_data: Users__Edit):
    with Session(engine) as db:
        row = db.get(Users__Base, item_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)

        sbda = db.get(Departments__Base, body_data.sbda)
        if not sbda:
            raise HTTPException(status_code=400, detail="invalid department")

        body_data_dump = body_data.model_dump(exclude_unset=True)
        row.sqlmodel_update(body_data_dump)
        db.add(row)
        db.commit()
        db.refresh(row)
        return row


@router.delete(
    "/{user_id}",
    response_model=Users,
    responses={404: {"description": "Not found"}},
)
def delete_user(item_id: int):
    with Session(engine) as db:
        row = db.get(Users__Base, item_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        row.is_deleted = 1
        db.add(row)
        db.commit()
        db.refresh(row)
        return row
