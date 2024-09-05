from fastapi import APIRouter, HTTPException, Query, Response, status
from sqlmodel import Session, select, delete, or_, and_
from sqlalchemy import exc

from db import engine
from db.models.experiments import *
from db.models import Link__Experiments_Related

router = APIRouter(
    prefix="/experiments",
    tags=["Experiments"],
)


@router.get(
    "/{experiment_id}/related",
    response_model=list[Experiment],
    responses={404: {"description": "Not found"}},
)
def list_related_experiments(experiment_id: int):
    with Session(engine) as db:
        experiment = db.get(Experiment__Base, experiment_id)
        if not experiment or experiment.is_deleted:
            raise HTTPException(status_code=404)

        related = (
            select(Link__Experiments_Related)
            .where(
                or_(
                    Link__Experiments_Related.experiment_1 == experiment_id,
                    Link__Experiments_Related.experiment_2 == experiment_id,
                )
            )
            .subquery("related")
        )

        rows = (
            select(Experiment__Base)
            .where(Experiment__Base.is_deleted == 0, Experiment__Base.id != experiment_id)
            .join(
                related,
                or_(
                    Experiment__Base.id == related.c.experiment_1,
                    Experiment__Base.id == related.c.experiment_2,
                ),
            )
        )

        return db.exec(rows).all()


@router.patch(
    "/{experiment_id}/related/{related_id}",
    response_model=Link__Experiments_Related,
    responses={404: {"description": "Not found"}},
)
def relate_an_experiment(experiment_id: int, related_id: int, response: Response):
    with Session(engine) as db:
        experiment = db.get(Experiment__Base, experiment_id)
        if not experiment or experiment.is_deleted:
            raise HTTPException(status_code=404)

        experiment_related = db.get(Experiment__Base, related_id)
        if not experiment_related or experiment_related.is_deleted:
            raise HTTPException(status_code=404)

        row = Link__Experiments_Related()
        row.experiment_1 = experiment_id
        row.experiment_2 = related_id
        db.add(row)
        db.commit()
        db.refresh(row)

        response.status_code = status.HTTP_201_CREATED

        return row


@router.delete(
    "/{experiment_id}/related/{related_id}",
    responses={404: {"description": "Not found"}},
    status_code=204,
)
def remove_experiment_relationship(experiment_id: int, related_id: int):

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

        these_links = db.exec(
            select(Link__Experiments_Related).where(
                or_(
                    and_(
                        Link__Experiments_Related.experiment_1 == experiment_id,
                        Link__Experiments_Related.experiment_2 == related_id,
                    ),
                    and_(
                        Link__Experiments_Related.experiment_1 == related_id,
                        Link__Experiments_Related.experiment_2 == experiment_id,
                    ),
                )
            )
        ).all()

        if not these_links:
            raise HTTPException(status_code=404)

        for i in these_links:
            db.delete(i)
        db.commit()
