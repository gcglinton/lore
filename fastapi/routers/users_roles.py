from fastapi import APIRouter, HTTPException, Query, Response, status
from sqlmodel import Session, select

from db import engine
from db.models.users_roles import *

router = APIRouter(
    prefix="/users/roles",
    tags=["Users - Roles"],
)


@router.get("/", response_model=list[User_Role])
def list_user_roles(offset: int = 0, limit: int = Query(default=100, le=100)):
    with Session(engine) as db:
        statement = (
            select(User_Role__Base)
            .where(User_Role__Base.is_deleted == 0)
            .offset(offset)
            .limit(limit)
        )
        return db.exec(statement).all()


@router.get(
    "/{role_id}",
    response_model=User_Role,
    responses={404: {"description": "Not found"}},
)
def get_one_user_role(role_id: int):
    with Session(engine) as db:
        row = db.get(User_Role__Base, role_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        return row


@router.post("/", response_model=User_Role, status_code=201)
def add_user_role(body_data: User_Role__Edit, response: Response):
    with Session(engine) as db:
        new_data = User_Role__Base()
        for attribute, value in body_data.__dict__.items():
            setattr(new_data, attribute, value)
        db.add(new_data)
        db.commit()
        db.refresh(new_data)

        response.status_code = status.HTTP_201_CREATED
        return new_data


@router.put(
    "/{role_id}",
    response_model=User_Role,
    responses={404: {"description": "Not found"}},
)
def update_user_role(role_id: int, body_data: User_Role__Edit):
    with Session(engine) as db:
        row = db.get(User_Role__Base, role_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        body_data_dump = body_data.model_dump(exclude_unset=True)
        row.sqlmodel_update(body_data_dump)
        db.add(row)
        db.commit()
        db.refresh(row)
        return row


@router.delete(
    "/{role_id}",
    responses={404: {"description": "Not found"}},
    status_code=204,
)
def delete_user_role(role_id: int):
    with Session(engine) as db:
        row = db.get(User_Role__Base, role_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        row.is_deleted = 1
        db.add(row)
        db.commit()
        db.refresh(row)
        return row
