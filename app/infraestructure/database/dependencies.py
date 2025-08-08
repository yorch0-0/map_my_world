from typing import Annotated
from fastapi import Depends
from sqlmodel import Session

from app.infraestructure.database.config import engine


def get_database_session():
    with Session(engine) as session:
        yield session


DatabaseSessionDep = Annotated[Session, Depends(get_database_session)]