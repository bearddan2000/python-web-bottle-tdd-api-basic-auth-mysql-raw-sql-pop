from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..connection.settings import *

engine = create_engine(
    '{engine}://{username}:{password}@{host}/{db_name}'.format(
        **MYSQL
    ),
    echo=SQLALCHEMY['debug']
)
session_local = sessionmaker(
    bind=engine,
    autoflush=SQLALCHEMY['autoflush'],
    autocommit=SQLALCHEMY['autocommit']
)

def get_db():
    db: sessionmaker = session_local()
    try:
        yield db
    finally:
        db.close()
