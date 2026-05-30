from schema import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///pokemon.db")

SessionLocal = sessionmaker(engine)


def init_db():
    Base.metadata.create_all(engine)
