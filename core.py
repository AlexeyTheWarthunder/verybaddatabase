from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

class PreBase:
    pass

base = declarative_base(cls=PreBase)

engine = create_engine('sqlite:///name_db.db', echo=False)
session = sessionmaker(bind=engine)


def init_db():
    base.metadata.create_all(bind=engine)