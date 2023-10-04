from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional
from . import scheema_moduleMaster

class show(BaseModel):
    SubModuleCode : int 
    SubModuleName : str
    ModuleCode : int
    module : scheema_moduleMaster.showsubmodule
    IndexNum : int
    SubModuleImage : Optional[str] 
    IsActive  : str
    AddedBy : int 
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):

    SubModuleName : str
    ModuleCode : int
    IndexNum : int
    SubModuleImage : str
    IsActive  : str
    AddedBy : int 
    
class update(BaseModel):
    SubModuleName : str
    ModuleCode : int
    IndexNum : int
    SubModuleImage : str
    IsActive  : str 
    ModifiedBy : int
    
        
class showfromsubmodule(BaseModel):
    SubModuleCode : int
    SubModuleName : str
    class Config:
        orm_mode=True       