import datetime
import uuid

from db import engine
from db.models import Experiment__Base, User__Base
from db.models.lessons_learned import *
from sqlmodel import Session, and_, col, select

from fastapi import APIRouter, HTTPException, Query, Response, status

router = APIRouter(
    prefix="/lessons_learned",
    tags=["Lessons Learned"],
)


@router.get("/", response_model=list[Lessons_Learned])
def list_lessons_learned(
    offset: int = 0,
    limit: int = Query(default=100, le=100),
    experiment: int = None,
    user: int = None,
):
    with Session(engine) as db:
        statement = select(Lessons_Learned__Base).where(
            Lessons_Learned__Base.is_deleted == 0
        )

        filters = []
        if experiment:
            filters.append(Lessons_Learned__Base.experiment_id == experiment)
        if user:
            filters.append(Lessons_Learned__Base.user_id == user)

        if filters:
            statement = statement.where(and_(*filters))

        statement.offset(offset).limit(limit)
        return db.exec(statement).all()


@router.get(
    "/{lessons_learned_id}",
    response_model=Lessons_Learned,
    responses={404: {"description": "Not found"}},
)
def get_one_lessons_learned(lessons_learned_id: int):
    with Session(engine) as db:
        row = db.get(Lessons_Learned__Base, lessons_learned_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        return row


@router.post(
    "/",
    response_model=Lessons_Learned,
    responses={400: {"description": "invalid references"}},
    status_code=201,
)
def submit_a_lessons_learned(body_data: Lessons_Learned__Submit, response: Response):
    with Session(engine) as db:
        new_data = Lessons_Learned__Base()
        for attribute, value in body_data.__dict__.items():
            setattr(new_data, attribute, value)

        experiment = db.get(Experiment__Base, body_data.experiment_id)
        if not experiment:
            raise HTTPException(status_code=400, detail="invalid experiment")

        user = db.get(User__Base, body_data.user_id)
        if not user:
            raise HTTPException(status_code=400, detail="invalid user")

        db.add(new_data)
        db.commit()
        db.refresh(new_data)

        response.status_code = status.HTTP_201_CREATED
        return new_data


@router.post(
    "/send",
    response_model=list[Lessons_Learned__Sent],
    responses={400: {"description": "invalid references"}},
    status_code=202,
)
def send_lessons_learned(body_data: Lessons_Learned__Send, response: Response):
    with Session(engine) as db:
        experiment = db.get(Experiment__Base, body_data.experiment_id)
        if not experiment:
            raise HTTPException(status_code=400, detail="invalid experiment")

        sent_ids = []
        for user in Lessons_Learned__Send.users:
            user_deets = db.get(User__Base, user)
            if not user_deets:
                raise HTTPException(status_code=400, detail="invalid user")

            new_data = Lessons_Learned__Base()
            new_data.user_id = user
            new_data.experiment_id = Lessons_Learned__Send.experiment_id
            new_data.guid = uuid.uuid4()

            db.add(new_data)

            print(f"send email to {user_deets.email}; {new_data.guid=}")

            db.commit()
            db.refresh(new_data)

            sent_ids.append(new_data.id)

        sent_rows = (
            select(Lessons_Learned__Base, col(User__Base.email).label("user_email"))
            .join(User__Base)
            .where(col(Lessons_Learned__Base.id).in_(sent_ids))
        )

        response.status_code = status.HTTP_202_ACCEPTED
        return db.exec(sent_rows).all()


@router.put(
    "/{lessons_learned_id}",
    response_model=Lessons_Learned,
    responses={404: {"description": "Not found"}},
)
def update_lessons_learned(lessons_learned_id: int, body_data: Lessons_Learned__Submit):
    with Session(engine) as db:
        row = db.get(Lessons_Learned__Base, lessons_learned_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)

        experiment = db.get(Experiment__Base, body_data.experiment_id)
        if not experiment:
            raise HTTPException(status_code=400, detail="invalid experiment")

        user = db.get(User__Base, body_data.user_id)
        if not user:
            raise HTTPException(status_code=400, detail="invalid user")

        body_data_dump = body_data.model_dump(exclude_unset=True)
        row.sqlmodel_update(body_data_dump)
        db.add(row)
        db.commit()
        db.refresh(row)
        return row


@router.delete(
    "/{lessons_learned_id}",
    responses={404: {"description": "Not found"}},
    status_code=204,
)
def delete_lessons_learned(lessons_learned_id: int):
    with Session(engine) as db:
        row = db.get(Lessons_Learned__Base, lessons_learned_id)
        if not row or row.is_deleted:
            raise HTTPException(status_code=404)
        row.is_deleted = 1
        db.add(row)
        db.commit()
        db.refresh(row)
