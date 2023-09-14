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

class Currency(Base):
    __tablename__ = 'tbl_CurrencyMaster'
    CurrencyCode = Column(Integer, primary_key=True, index=True ,autoincrement=True)
    CurrencyName = Column(String(50))
    Currency_image = Column(String)
    CurrencySymbol = Column(String(10))
    ShortName = Column(String(5))
    AddedBy = Column(Integer, nullable=False)
    AddedOn = Column(DateTime, default=func.now(), nullable=False)
    ModifiedBy = Column(Integer)
    ModifiedOn = Column(DateTime) 
    locations = relationship("LocationMaster", back_populates="currency")
    
class LocationMaster(Base):
    __tablename__ = 'tbl_LocationMaster' 
    LocationCode = Column(Integer, primary_key=True, index=True ,autoincrement=True)
    LocationName =Column(String)
    ShortName = Column(String)
    CurrencyCode = Column(Integer,ForeignKey('tbl_CurrencyMaster.CurrencyCode') )
    TimeZoneCode =Column(String)
    IsActive = Column(String,nullable=False)
    AddedBy = Column(Integer,nullable=False)
    AddedOn = Column(DateTime, default=func.now(), nullable=False)
    ModifiedBy = Column(Integer)
    ModifiedOn = Column(Integer) 
    currency = relationship("Currency", back_populates="locations")


