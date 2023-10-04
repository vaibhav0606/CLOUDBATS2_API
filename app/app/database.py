
import pymssql
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from databases import Database

DATABASE_URL = "mssql+pymssql://bats:Bats212#@202.38.173.95/PYBATS"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def Connect_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
