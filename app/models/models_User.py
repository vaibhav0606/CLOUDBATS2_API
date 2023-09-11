import uuid
from sqlalchemy import Column, Integer, String, ForeignKey,Boolean
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
from sqlalchemy.sql import func
from pydantic import BaseModel, Field
from sqlalchemy.orm import relationship



Base = declarative_base()


 
class User(Base):    
    __tablename__ = 'User'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, nullable=False, unique=True, default=uuid.uuid4)
    Email = Column(String)
    Object_Status = Column(String, nullable=False)
    Password = Column(String)
    Person_Id = Column(UNIQUEIDENTIFIER, nullable=False)
    RememberMe = Column(Boolean, nullable=False)
    Role_Id = Column(UNIQUEIDENTIFIER, nullable=False)
    System = Column(Boolean, nullable=False)

class User_login(Base):
    __tablename__ = "BTS_logins"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    userid = Column(Integer)
    access_token = Column(String)
    token_type= Column(String)
    AddedOn =Column(String)
    status =Column(Integer)
