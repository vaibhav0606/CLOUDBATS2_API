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

class ContentTypeMaster(Base):
    __tablename__ = 'tbl_ContentTypeMaster'

    ContentTypeCode = Column(Integer, primary_key=True, autoincrement=True)
    ContentTypeName = Column(String(50), nullable=False)
    MultiPart = Column(Integer)
    EpisodeSpecific = Column(Integer)
    LiveEvent = Column(Integer)
    SportEvent = Column(Integer)
    IsActive = Column(Integer, nullable=False)
    AddedBy = Column(Integer, nullable=False)
    AddedOn = Column(DateTime, nullable=False, default=func.now())
    ModifiedBy = Column(Integer)
    ModifiedOn = Column(DateTime)
    
    
class SubGenreMaster(Base):
    __tablename__ = 'tbl_SubGenreMaster'

    SubGenreCode = Column(Integer, primary_key=True, autoincrement=True)
    SubGenreName = Column(String(50))
    IsActive = Column(Integer, nullable=False)
    AddedBy = Column(Integer, nullable=False)
    AddedOn = Column(DateTime, nullable=False, default=func.now())
    ModifiedBy = Column(Integer)
    ModifiedOn = Column(DateTime)


class AwardMaster(Base):
    __tablename__ = 'tbl_AwardMaster'

    AwardCode = Column(Integer, primary_key=True, autoincrement=True)
    AwardName = Column(String(100))
    AwardDate = Column(DateTime)
    IsActive = Column(Integer, nullable=False)
    AddedBy = Column(Integer, nullable=False)
    AddedOn = Column(DateTime, nullable=False, default=func.now())
    ModifiedBy = Column(Integer)
    ModifiedOn = Column(DateTime)
