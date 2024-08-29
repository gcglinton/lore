
## Database Setup

The project is currently using an SQLite database because it's simple, but will likely transition to PostgreSQL, MySQL, or MSSQL at some point in order to provide better cloud operations.

To setup the database, you'll need to run `python manage.py migrate` from withtin the `src` directory. This will create/update the SQLite file, all the required tables, and rows required to run the application.

If you wish to access the admin interface, you'll need to run `python manage.py createsuperuser` to create an administrative user.

## Running 

This is a very standard Django project, so running a local server is as simple as running `python manage.py runserver`, and openning a browser to `http://127.0.0.1:8000/`.

There is currently only a single application in the Django project, for the Client Relationship Manager (CRM). Eventually there will likely be a number of other applications for various other features/interfaces required by the team.

The CRM itself is served at `http://127.0.0.1:8000/crm`, and the Django administrative interface is at `http://127.0.0.1:8000/admin`.

You can change the port that it's listening on (if you wanted to run both this, and the FastAPI demo at the same time), by specifying a port to `manage.py`, like `python manage.py runserver 8002`, and then all requests above would need to use that new port.