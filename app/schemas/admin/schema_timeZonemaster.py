from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional

class show(BaseModel):
    TimeZoneCode : int 
    TimeZoneName : str
    ShortName :  str
    IsActive  : int
    AddedBy : int
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    TimeZoneName : str
    ShortName :  str
    IsActive  : int
    
class update(add):
   pass
    
class postout(BaseModel):
    ModuleName : str
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    ModuleName : str
    code : str = "200"
    status : str = "Updated"
    
        
class showmodule(BaseModel):
    ModuleCode : int
    ModuleName : str
  
  

class loaddropdown(BaseModel):
    ModuleCode : int
    ModuleName : str
    class Config:
        orm_mode=True