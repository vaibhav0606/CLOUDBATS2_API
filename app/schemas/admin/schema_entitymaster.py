from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class show(BaseModel):
    EntityCode : int
    EntityName : str
    PermAddress : str
    CorpAddress : Optional[str]
    ContactPerson : str
    Contact : str
    IsActive :int
    AddedBy : int 
    AddedOn : datetime
    PANNO : Optional[str]
    CINNumber : Optional[str]
    class Config:
        orm_mode=True
     
class add(BaseModel):
    EntityName : str
    PermAddress : str
    CorpAddress : str
    ContactPerson : str
    Contact : str
    IsActive :int
    PANNO : str
    CINNumber : str
    
class update(add):
   pass
    
class postout(BaseModel):
    EntityName : str
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    EntityName : str
    code : str = "200"
    status : str = "Updated"
    
class showentity(BaseModel):
    EntityCode : int
    EntityName : str
    

class loaddropdown(BaseModel):
    EntityCode : int
    EntityName : str
    class Config:
        orm_mode=True
   