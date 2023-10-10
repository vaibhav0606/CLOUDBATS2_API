from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .schema_moduleMaster import showmodule

class show(BaseModel):
    SubModuleCode : int 
    SubModuleName : str
    ModuleCode : int
    module : showmodule
    IndexNum : int
    SubModuleImage : Optional[str] 
    IsActive  : int
    AddedBy : int 
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):

    SubModuleName : str
    ModuleCode : int
    IndexNum : int
    SubModuleImage : str
    IsActive  : int
    
class update(add):
   pass

class postout(BaseModel):
    SubModuleName : str
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    SubModuleName : str
    code : str = "200"
    status : str = "Updated"
    
        
class showsubmodule(BaseModel):
    SubModuleCode : int
    SubModuleName : str
    

class loaddropdown(BaseModel):
    SubModuleCode : int
    SubModuleName : str
    class Config:
        orm_mode=True
   