from fastapi import APIRouter, HTTPException, Query, Response, status
from sqlmodel import Session, select

from db import engine
from db.models.users import *
from db.models.departments import Department__Base

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/", response_model=list[User])
def list_users(offset: int = 0, limit: int = Query(default=100, le=100)):
    with Session(engine) as db:
        statement = (
            select(User__Base)
            .where(User__Base.is_deleted == 0)
            .offset(offset)
            .limit(limit)
        )
        return db.exec(statement).all()


@router.get(
    "/{user_id}",
    response_model=User,
    responses={404: {"description": "Not found"}},
)
def get_one_user(user_id: int):
    with Session(engine) as db:
        row = db.get(User__Base, user_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        return row


@router.post(
    "/",
    response_model=User,
    responses={400: {"description": "invalid references"}},
    status_code=201,
)
def add_user(body_data: User__Edit, response: Response):
    with Session(engine) as db:
        new_data = User__Base()
        for attribute, value in body_data.__dict__.items():
            setattr(new_data, attribute, value)

        department = db.get(Department__Base, body_data.department)
        if not department:
            raise HTTPException(status_code=400, detail="invalid department")
        db.add(new_data)
        db.commit()
        db.refresh(new_data)

        response.status_code = status.HTTP_201_CREATED
        return new_data


@router.put(
    "/{user_id}",
    response_model=User,
    responses={404: {"description": "Not found"}},
)
def update_user(user_id: int, body_data: User__Edit):
    with Session(engine) as db:
        row = db.get(User__Base, user_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)

        department = db.get(Department__Base, body_data.department)
        if not department:
            raise HTTPException(status_code=400, detail="invalid department")

        body_data_dump = body_data.model_dump(exclude_unset=True)
        row.sqlmodel_update(body_data_dump)
        db.add(row)
        db.commit()
        db.refresh(row)
        return row


@router.delete(
    "/{user_id}",
    responses={404: {"description": "Not found"}},
    status_code=204,
)
def delete_user(user_id: int):
    with Session(engine) as db:
        row = db.get(User__Base, user_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        row.is_deleted = 1
        db.add(row)
        db.commit()
        db.refresh(row)
