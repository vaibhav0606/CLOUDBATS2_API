from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional

class show(BaseModel):
    ZoneCode : int
    ZoneName : str
    ShortName : str
    IsActive  : int
    AddedBy : int 
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    ZoneName : str
    ShortName : str
    IsActive  : int
    
class update(add):
    pass
    
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
    
class loaddropdown(BaseModel):
    ZoneCode: int
    ZoneName : str
    class Config:
        orm_mode=True