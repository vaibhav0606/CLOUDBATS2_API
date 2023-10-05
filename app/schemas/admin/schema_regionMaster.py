from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional
from . import schema_zoneMaster

class show(BaseModel):
    RegionCode : int
    RegionName : str
    ShortName : str
    Zone : schema_zoneMaster.showzone
    IsActive  : int
    AddedBy : int 
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    RegionName : str
    ShortName : str
    ZoneCode : int
    IsActive  : int
    
class update(BaseModel):
    pass 
    
class postout(BaseModel):
    RegionName : str
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    RegionName : str
    code : str = "200"
    status : str = "Updated"
    
class showregion(BaseModel):
    RegionCode : int
    RegionName : str