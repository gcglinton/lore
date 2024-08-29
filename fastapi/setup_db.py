from sqlmodel import Field, Session, SQLModel, create_engine

from model import Hero

sqlite_file_name = "db.sqlite3"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_heroes():
    heros = [
        Hero(name="Deadpond", secret_name="Dive Wilson"),
        Hero(name="Spider-Boy", secret_name="Pedro Parqueador"),
        Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
    ]

    with Session(engine) as session:
        for h in heros:
            session.add(h)

        session.commit()


def main():
    create_heroes()


if __name__ == "__main__":
    main()