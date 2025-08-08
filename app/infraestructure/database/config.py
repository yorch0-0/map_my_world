import os

from dotenv import load_dotenv
from sqlmodel import create_engine, SQLModel

load_dotenv()

database_url = os.getenv('DATABASE_URL')

engine = create_engine(database_url)


def init_db():
    SQLModel.metadata.create_all(engine)
