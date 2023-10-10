from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional

class show(BaseModel):
    ModuleCode : int 
    ModuleName : Optional[str]
    IndexNum :  Optional[int]
    ModuleImage : Optional[str]
    IsActive  : int
    AddedBy : int
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    ModuleName : str
    IndexNum : int
    ModuleImage : str
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

  