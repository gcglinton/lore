
## Context

This sample is using [FastAPI](https://fastapi.tiangolo.com/) for it's API interface handler, [SQLModel](https://sqlmodel.tiangolo.com/) as it's ORM, and [Alembic](https://alembic.sqlalchemy.org/en/latest/index.html) to manage it's DB migrations (automatic schema tracking)

## Database Setup

The project is currently using an SQLite database because it's simple, but will likely transition to PostgreSQL, MySQL, or MSSQL at some point in order to provide better cloud operations.

To setup the database, you'll need to run `alembic upgrade head` from withtin this directory. This will create/update the SQLite file, and all the required tables required.

Then to insert some data, run `python setup_db.py`.

## Running 

This is a very standard Django project, so running a local server is as simple as running `fastapi dev main.py`, and openning a browser to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

This is an API, with no front-end, so there's nothing to really open in the browser (or there is, but it's not interesting). You can check out [http://127.0.0.1:8000/items/](http://127.0.0.1:8000/items/) for a DB-less route, or [http://127.0.0.1:8000/heros/](http://127.0.0.1:8000/heros/) for one that queries the DB.

FastAPI has a built-in documentation engine, which you can see at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs), or [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)