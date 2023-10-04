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
 
    
    
    

    
