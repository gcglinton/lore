from fastapi import APIRouter, HTTPException, Query, Response, status
from sqlmodel import Session, select, delete, or_, and_
from sqlalchemy import exc

from db import engine
from db.models.experiments import *
from db.models import Link__Experiments_Users, Experiment_Users
from db.models import User__Base, User_Role__Base


router = APIRouter(
    prefix="/experiments",
    tags=["Experiments"],
)


@router.get(
    "/{experiment_id}/users",
    response_model=list[Experiment_Users],
    responses={404: {"description": "Not found"}},
)
def list_experiment_users(experiment_id: int):

    with Session(engine) as db:
        experiment = db.get(Experiment__Base, experiment_id)
        if not experiment or experiment.is_deleted:
            raise HTTPException(status_code=404)

        user_links = (
            select(Link__Experiments_Users)
            .where(Link__Experiments_Users.experiment_id == experiment_id)
            .subquery("user_links")
        )

        rows = (
            select(User_Role__Base, User__Base)
            .where(
                User__Base.is_deleted == 0,
                User_Role__Base.id == user_links.c.role_id,
            )
            .join(user_links, User__Base.id == user_links.c.user_id)
        )

        return_data = []
        for r in db.exec(rows).all():
            return_data.append(
                Experiment_Users(
                    user_id=r.Users__Base.id,
                    user_name_first=r.Users__Base.name_first,
                    user_name_last=r.Users__Base.name_last,
                    user_email=r.Users__Base.email,
                    role_id=r.Users_Roles__Base.id,
                    role_name=r.Users_Roles__Base.name,
                )
            )

        return return_data


@router.get(
    "/{experiment_id}/users/cloud",
    response_model=list[Experiment_CloudGroup],
    responses={
        404: {"description": "Not found"},
        502: {"description": "Upstream API encountered errors"},
    },
)
def list_cloud_experiment_users(experiment_id: int):

    with Session(engine) as db:
        experiment = db.get(Experiment__Base, experiment_id)
        if not experiment or experiment.is_deleted:
            raise HTTPException(status_code=404)

    from urllib import request
    import json
    import os

    AZ_FUNCTION_URL = os.getenv("AZ_FUNCTION_URL")
    AZ_FUNCTION_CODE = os.getenv("AZ_FUNCTION_CODE")

    url = f"{AZ_FUNCTION_URL}{AZ_FUNCTION_CODE}"

    req = request.Request(
        url,
        method="POST",
    )
    req.add_header("Content-Type", "application/json")
    print(f"{url=}")
    print(f"{experiment.environment_name=}")

    req_data = json.dumps({"experimentname": experiment.environment_name}).encode()
    r = request.urlopen(req, data=req_data)
    if r.status != 200:
        raise HTTPException(status_code=502)

    lines = r.read().decode().splitlines()

    if "The function was called by" in lines[0]:
        lines = lines[1:]

    ret_data = json.loads("\n".join(lines))

    return_data = []
    return ret_data


@router.patch(
    "/{experiment_id}/users/{user_id}/role/{role_id}",
    response_model=Link__Experiments_Users,
    responses={
        404: {"description": "Not found"},
        204: {"description": "User added to experiment with defined role"},
    },
)
def add_user_to_experiment(experiment_id: int, user_id: int, role_id: int, response: Response):

    with Session(engine) as db:
        experiment = db.get(Experiment__Base, experiment_id)
        if not experiment or experiment.is_deleted:
            raise HTTPException(status_code=404, detail="invalid experiment")

        user = db.get(User__Base, user_id)
        if not user or user.is_deleted:
            raise HTTPException(status_code=400, detail="invalid user")

        role = db.get(User_Role__Base, role_id)
        if not role or role.is_deleted:
            raise HTTPException(status_code=400, detail="invalid role")

        row = Link__Experiments_Users()
        row.experiment_id = experiment_id
        row.user_id = user_id
        row.role_id = role_id
        try:
            db.add(row)
            db.commit()
            db.refresh(row)
        except exc.IntegrityError:
            raise HTTPException(status_code=304, detail="invalid role")

        response.status_code = status.HTTP_201_CREATED
        return row


@router.delete(
    "/{experiment_id}/users/{user_id}/role/{role_id}",
    responses={404: {"description": "Not found"}},
    status_code=204,
)
def remove_user_from_experiment(experiment_id: int, user_id: int, role_id: int):

    with Session(engine) as db:
        # experiment = db.get(Experiments__Base, experiment_id)
        # if not experiment or experiment.is_deleted:
        #     raise HTTPException(status_code=404, detail="invalid experiment")

        # user = db.get(Users__Base, user_id)
        # if not user or user.is_deleted:
        #     raise HTTPException(status_code=400, detail="invalid user")

        # role = db.get(Users_Roles__Base, role_id)
        # if not role or role.is_deleted:
        #     raise HTTPException(status_code=400, detail="invalid role")

        this_link = db.exec(
            select(Link__Experiments_Users).where(
                Link__Experiments_Users.experiment_id == experiment_id,
                Link__Experiments_Users.user_id == user_id,
                Link__Experiments_Users.role_id == role_id,
            )
        ).first()

        if not this_link:
            raise HTTPException(status_code=404)

        print(this_link)

        db.delete(this_link)
        db.commit()
