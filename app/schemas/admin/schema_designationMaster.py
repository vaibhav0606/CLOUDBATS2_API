from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional

class show(BaseModel):
    DesignationCode : int
    DesignationName : str
    ShortName : str
    IsActive  : int
    AddedBy : int 
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    DesignationName : str
    ShortName : str
    IsActive  : int
    
class update(add):
    pass
    
class postout(BaseModel):
    DesignationName : str
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    DesignationName : str
    code : str = "200"
    status : str = "Updated"
    
class showdesignation(BaseModel):
    DesignationCode : int
    DesignationName : str
    

class loaddropdown(BaseModel):
    DesignationCode : int
    DesignationName : str
    class Config:
        orm_mode=True