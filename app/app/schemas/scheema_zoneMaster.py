from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional

class show(BaseModel):
    ZoneCode : int
    ZoneName : str
    ShortName : str
    IsActive  : str
    AddedBy : int 
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    ZoneName : str
    ShortName : str
    IsActive  : str
    AddedBy : int 
    
class update(BaseModel):
    ZoneName : str
    ShortName : str
    IsActive  : str 
    ModifiedBy : int
    
    
class showregionzone(BaseModel):
    ZoneCode: int
    ZoneName : str