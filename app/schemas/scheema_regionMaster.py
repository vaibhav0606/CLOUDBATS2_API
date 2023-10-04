from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional
from . import scheema_zoneMaster

class show(BaseModel):
    RegionCode : int
    RegionName : str
    ShortName : str
    Zone : scheema_zoneMaster.showregionzone
    IsActive  : str
    AddedBy : int 
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    RegionName : str
    ShortName : str
    ZoneCode : int
    IsActive  : str
    AddedBy : int 
    
class update(BaseModel):
    RegionName : str
    ShortName : str
    ZoneCode : int
    IsActive  : str 
    ModifiedBy : int