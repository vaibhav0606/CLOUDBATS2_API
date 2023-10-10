from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional

class show(BaseModel):
    StarCastTypeCode : int
    StarCastTypeName : str
    IsActive  : int
    AddedBy : int 
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    StarCastTypeName: str
    IsActive  : int
    
class update(add):
    pass 

class postout(BaseModel):
    StarCastTypeName : str
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    StarCastTypeName : str
    code : str = "200"
    status : str = "Updated"

class showstarcasttype(BaseModel):
    StarCastTypeCode : int
    StarCastTypeName : str

class loaddropdown(BaseModel):
    StarCastTypeCode : int
    StarCastTypeName : str
    class Config:
        orm_mode=True
