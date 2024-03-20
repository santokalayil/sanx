from pathlib import Path
import pandas as pd
from typing import List, Optional, Tuple
from typing import Optional
from sqlmodel import Field, SQLModel, Session, create_engine, select
import json
from cachetools import cached, TTLCache

from sanx.db.models import User

DBPATH = Path(__file__).parent / "db.sqlite3"
ENGINE = create_engine(f"sqlite:///{str(DBPATH)}")


def to_df(objects: List[SQLModel], cols: Optional[Tuple[str]] = None) -> pd.DataFrame:
    """Converts SQLModel objects into a Pandas DataFrame.
    Usage
    ----------
    df = sqlmodel_to_df(list_of_sqlmodels)
    Parameters
    ----------
    :param objects: List[SQLModel]: List of SQLModel objects to be converted.
    """
    df = pd.DataFrame.from_records(map(dict, objects))

    return df[list(cols)] if (cols and len(df.columns)) else df  # .iloc[:, 1:]


# admin_user = User(
#     name="Santo", employee_id="76248", access_level=json.dumps(["admin", "standard"])
# )
# standard_user = User(
#     name="Sajan", employee_id="87676", access_level=json.dumps(["standard"])
# )

# SQLModel.metadata.create_all(ENGINE)
# with Session(ENGINE) as session:
#     session.add(standard_user)
#     session.add(admin_user)
#     session.commit()

# Create a TTLCache for caching user data
user_cache = TTLCache(maxsize=100, ttl=300)


@cached(user_cache)
def get_users(name: Optional[str] = None, cols: Optional[Tuple[str]] = None):
    global ENGINE
    with Session(ENGINE) as session:
        statement = (
            select(User).where(User.name.like(f"%{name}%")) if name else select(User)
        )
        # statement = select(User).where(User.name == name) if name else select(User)
        users = session.exec(statement).fetchall()
        return to_df(users, cols)


# REFERENCE_CODE -------- from here to end
class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


if not DBPATH.exists():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
    engine = create_engine(f"sqlite:///{str(DBPATH)}")
    SQLModel.metadata.create_all(engine)

    hero_1.model_fields

    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        session.commit()


# with Session(engine) as session:
#     statement = select(Hero).where(Hero.name == "Spider-Boy")
#     hero = session.exec(statement).first()
#     print(hero.model_dump())


def get_hero_rows(name, cols: Optional[List[str]] = None):
    global ENGINE
    with Session(ENGINE) as session:
        statement = select(Hero).where(Hero.name == name)
        heros = session.exec(statement).fetchall()
        return to_df(heros, cols)
