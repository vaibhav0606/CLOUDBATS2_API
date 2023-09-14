import uuid
from sqlalchemy import Column, Integer, String, ForeignKey,Boolean
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,DateTime,BigInteger
from app.database import Base
from sqlalchemy.sql import func
from pydantic import BaseModel, Field
from sqlalchemy.orm import relationship

Base = declarative_base()
 
class loginmaster(Base):    
    __tablename__ = 'tbl_LoginMaster'

    LoginCode = Column(BigInteger, primary_key=True, nullable=False)
    LoginName = Column(String)
    Password = Column(String)
    EmployeeCode = Column(BigInteger, nullable=False)
    DefaultLocChnlCode = Column(String)
    RegisteredMobileNo = Column(String(10))
    MPIN = Column(String(4))
    TPIN = Column(String(4))
    IsFinalize = Column(String(1))
    IsAdmin = Column(String(1))
    SuperAdmin = Column(String(1))
    IsActive = Column(String(1),nullable=False)
    AddedBy = Column(BigInteger,nullable=False)
    AddedOn = Column(DateTime, default=func.now(), nullable=False)
    ModifiedBy = Column(Integer)
    ModifiedOn = Column(Integer)

class loginmaster_token(Base):
    __tablename__ = "tbl_login_token"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    LoginCode = Column(BigInteger)
    access_token = Column(String)
    token_type= Column(String)
    AddedOn =Column(String)
    status =Column(Integer)
    
    
