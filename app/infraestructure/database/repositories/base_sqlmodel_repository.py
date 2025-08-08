from abc import ABC

from sqlmodel import Session

from app.infraestructure.database.dependencies import DatabaseSessionDep


class BaseSqlModelRepository(ABC):
    db_session: Session

    def __init__(self, session: DatabaseSessionDep):
        self.db_session = session
