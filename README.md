# LORE

> [!NOTE]  
> This project is in very early stages of development, and is almost certainly going to change/break substantially.

This is the fully custom-built evolution (pun intended) of the SSC Science Program's forray into building a CRM using some low-code/no-code projects; namely Budibase.

While Budibase is quite powerful, it has many limitations in how it operates, builds UIs, and can be used. Some of those limitations are inherent to the way the platform is desgined and built, but others are as a result of being gated behind a paywall.

It was always widely suspected that we would end up building our own, and this is the start of that process.

## Platform

There's two sample apps in this repo. 

The team has a fair amount of knowledge with Python, and it should serve as a good start. 

- `django` is written with [Django](https://www.djangoproject.com/)
- `fastapi` is an API platform using [FastAPI](https://fastapi.tiangolo.com/)

Those folder names might seem like nonsense, but I couldn't come up with anything better.

## Installtion

A Python interpreter is required (ideally something modern, a la 3.12+), along with `pip`.

I would strongly suggest creating a [virtual environment](https://virtualenvwrapper.readthedocs.io/en/latest/) in order to keep packages separate for this project, and ensure proper operation.

On Ubuntu 24.04:
```
sudo apt install python3-virtualenvwrapper
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
mkvirtualenv lore
```

With that configured, simply run `pip install -r requirements.txt` to install all the dependencies for everything here.

## How to use the application

Check README.md in each folder to see how to run them.

# DB Schema

While nothing is finalized, there's a dbdiagram.io DBML definition in `schema.txt`. It would need to be properly re-written for Django, or FastAPI/SQLAlchemy, but that shouldn't take too long. It's meant to be a rough clone of the current DB that LTPMS uses, with some optimizations (centralized user tables, lookups/references for all possible fields, etc..)