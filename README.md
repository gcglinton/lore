# LORE

> [!NOTE]  
> This project is in very early stages of development, and is almost certainly going to change/break substantially.

This is the fully custom-built evolution (pun intended) of the SSC Science Program's forray into building a CRM using some low-code/no-code projects; namely Budibase.

While Budibase is quite powerful, it has many limitations in how it operates, builds UIs, and can be used. Some of those limitations are inherent to the way the platform is desgined and built, but others are as a result of being gated behind a paywall.

It was always widely suspected that we would end up building our own, and this is the start of that process.

## Platform

This application is written with [Django](https://www.djangoproject.com/). The team has a fair amount of knowledge with Python, and it should serve as a good start. 

This will almost certainly change, as maybe Django isn't the right solution, and we should instead go with a front-end/backend model using *$language*/*$framwork*.

## Installtion

A Python interpreter is required, along with `pip`.

It is suggested to create a [virtual environment](https://virtualenvwrapper.readthedocs.io/en/latest/) in order to keep packages separate for this project, and ensure proper operation.

With that configured, simply run `pip install -r requirements.txt` to install all the dependencies for this project.

## How to use the application

### Database Setup

The project is currently using an SQLite database because it's simple, but will likely transition to PostgreSQL, MySQL, or MSSQL at some point in order to provide better cloud operations.

To setup the database, you'll need to run `python manage.py migrate` from withtin the `src` directory. This will create/update the SQLite file, all the required tables, and rows required to run the application.

If you wish to access the admin interface, you'll need to run `python manage.py createsuperuser` to create an administrative user.

### Running 


This is a very standard Django project, so running a local server is as simple as running `python manage.py runserver`, and openning a browser to `http://127.0.0.1:8000/`.

There is currently only a single application in the Django project, for the Client Relationship Manager (CRM). Eventually there will likely be a number of other applications for various other features/interfaces required by the team.

The CRM itself is served at `http://127.0.0.1:8000/crm`, and the Django administrative interface is at `http://127.0.0.1:8000/admin`.