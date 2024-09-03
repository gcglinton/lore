from fastapi import APIRouter, HTTPException, Query
from sqlmodel import Session, select

from db import engine
from db.models.users_roles import *

router = APIRouter(
    prefix="/users/roles",
    tags=["Users - Roles"],
)


@router.get("/", response_model=list[Users_Roles])
def list_user_roles(offset: int = 0, limit: int = Query(default=100, le=100)):
    with Session(engine) as db:
        statement = (
            select(Users_Roles__Base)
            .where(Users_Roles__Base.is_deleted == 0)
            .offset(offset)
            .limit(limit)
        )
        return db.exec(statement).all()


@router.get(
    "/{role_id}",
    response_model=Users_Roles,
)
def get_one_user_role(role_id: int):
    with Session(engine) as db:
        row = db.get(Users_Roles__Base, role_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        return row


@router.post("/", response_model=Users_Roles)
def add_user_role(body_data: Users_Roles__Edit):
    with Session(engine) as db:
        new_data = Users_Roles__Base()
        for attribute, value in body_data.__dict__.items():
            setattr(new_data, attribute, value)
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data


@router.put("/{role_id}", response_model=Users_Roles)
def update_user_role(item_id: int, body_data: Users_Roles__Edit):
    with Session(engine) as db:
        row = db.get(Users_Roles__Base, item_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        body_data_dump = body_data.model_dump(exclude_unset=True)
        row.sqlmodel_update(body_data_dump)
        db.add(row)
        db.commit()
        db.refresh(row)
        return row


@router.delete("/{role_id}", response_model=Users_Roles)
def delete_user_role(item_id: int):
    with Session(engine) as db:
        row = db.get(Users_Roles__Base, item_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        row.is_deleted = 1
        db.add(row)
        db.commit()
        db.refresh(row)
        return row
