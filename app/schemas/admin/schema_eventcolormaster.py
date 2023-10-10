
from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional
from .schema_moduleMaster import showmodule
from .schema_subModuleMaster import showsubmodule


class show(BaseModel):
    EventCode : int 
    EventName : str
    EventType : str
    EventDefaultFrontColor : str
    EventDefaultBackColor : str
    IsActive  : int
    AddedBy : int 
    AddedOn : datetime
    class Config:
        orm_mode=True
        
     
class add(BaseModel):
    EventName : str
    EventType : str
    EventDefaultFrontColor : str
    EventDefaultBackColor : str
    IsActive  : int
    
class update(add):
   pass
    
class postout(BaseModel):
    EventName : str
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    EventName : str
    code : str = "200"
    status : str = "Updated"
    

class loaddropdown(BaseModel):
    EventCode : int 
    EventName : str
    class Config:
        orm_mode=True
   

