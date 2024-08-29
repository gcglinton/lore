# LORE

> [!NOTE]  
> This project is in very early stages of development, and is almost certainly going to change/break substantially.

This is the fully custom-built evolution (pun intended) of the SSC Science Program's forray into building a CRM using some low-code/no-code projects; namely Budibase.

While Budibase is quite powerful, it has many limitations in how it operates, builds UIs, and can be used. Some of those limitations are inherent to the way the platform is desgined and built, but others are as a result of being gated behind a paywall.

It was always widely suspected that we would end up building our own, and this is the start of that process.

## Platform

There's two sample apps in this repo. 

The team has a fair amount of knowledge with Python, and it should serve as a good start. 

Everything in the `django` folder is is written with [Django](https://www.djangoproject.com/).
Everything in the `fastapi` folder is meant to be an backend API platform using FastAPI and SQLModel

## Installtion

A Python interpreter is required, along with `pip`.

It is suggested to create a [virtual environment](https://virtualenvwrapper.readthedocs.io/en/latest/) in order to keep packages separate for this project, and ensure proper operation.

With that configured, simply run `pip install -r requirements.txt` to install all the dependencies for this project.

## How to use the application

###

Check README.md in each folder to see how to run them.