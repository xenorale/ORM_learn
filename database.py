from sqlalchemy import create_engine
from sqlalchemy.orm import Session

DB_URL = "postgresql+psycopg://postgres:1234@localhost:5432/mydatabase"

engine = create_engine(DB_URL, echo=False)
session = Session(engine)
