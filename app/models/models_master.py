import uuid
from sqlalchemy import Column, Integer, String, ForeignKey,Boolean
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime,BigInteger
from app.database import Base
from sqlalchemy.sql import func
from pydantic import BaseModel, Field
from sqlalchemy.orm import relationship

Base = declarative_base()

class Currency(Base):
    __tablename__ = 'tbl_CurrencyMaster'
    CurrencyCode = Column(BigInteger, primary_key=True, index=True ,autoincrement=True)
    CurrencyName = Column(String(50))
    Currency_image = Column(String)
    CurrencySymbol = Column(String(10))
    ShortName = Column(String(5))
    AddedBy = Column(BigInteger, nullable=False)
    AddedOn = Column(DateTime, default=func.now(), nullable=False)
    ModifiedBy = Column(BigInteger)
    ModifiedOn = Column(DateTime) 
    locations = relationship("LocationMaster", back_populates="currency")
    
class LocationMaster(Base):
    __tablename__ = 'tbl_LocationMaster' 
    LocationCode = Column(BigInteger, primary_key=True, index=True ,autoincrement=True)
    LocationName =Column(String)
    ShortName = Column(String)
    CurrencyCode = Column(BigInteger,ForeignKey('tbl_CurrencyMaster.CurrencyCode') )
    TimeZoneCode =Column(String)
    IsActive = Column(String,nullable=False)
    AddedBy = Column(BigInteger,nullable=False)
    AddedOn = Column(DateTime, default=func.now(), nullable=False)
    ModifiedBy = Column(BigInteger)
    ModifiedOn = Column(DateTime) 
    currency = relationship("Currency", back_populates="locations")

  
class EntityMaster(Base):
    __tablename__ = 'tbl_EntityMaster' 
    EntityCode = Column(BigInteger, primary_key=True, index=True ,autoincrement=True)
    EntityId =Column(String(10))
    EntityName = Column(String(100))
    PermAddress = Column(String(500)) 
    CorpAddress =Column(String(500))
    ContactPerson=Column(String(25))
    Contact=Column(String(100))
    IsActive = Column(String(1))
    AddedBy = Column(BigInteger,nullable=False)
    AddedOn = Column(DateTime, default=func.now(), nullable=False)
    ModifiedBy = Column(BigInteger)
    ModifiedOn = Column(DateTime) 
    PANNO = Column(String(50))
    ServiceTaxNo = Column(String(50))
    CINNumber = Column(String(50))

class ChannelMaster(Base):
    __tablename__ = 'tbl_ChannelMaster' 
    ChannelCode = Column(BigInteger, primary_key=True, index=True ,autoincrement=True)
    ChannelName =Column(String(10))
    ShortName = Column(String(10))
    Channel_Image = Column(String(100)) 
    ChannelGenre = Column(String(50))
    ChannelContentType = Column(String(50))
    IsActive = Column(String(1))
    AddedBy = Column(BigInteger,nullable=False)
    AddedOn = Column(DateTime, default=func.now(), nullable=False)
    ModifiedBy = Column(BigInteger)
    ModifiedOn = Column(DateTime) 
    StateCode = Column(BigInteger)
    SACCode = Column(String(50))
    GSTN_id = Column(String(50))
