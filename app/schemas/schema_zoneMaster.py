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
    
class update(BaseModel):
    ZoneName : str
    ShortName : str
    IsActive  : str 
    
class postout(BaseModel):
    ZoneName : str
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    ZoneName : str
    code : str = "200"
    status : str = "Updated"
    
class showzone(BaseModel):
    ZoneCode: int
    ZoneName : str