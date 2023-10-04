from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional
from . import scheema_moduleMaster,scheema_subModuleMaster


class show(BaseModel):
    FormCode : int 
    FormName : str
    module : scheema_moduleMaster.showfrommodule
    SubModule : scheema_subModuleMaster.showfromsubmodule
    IndexNum : Optional[int]
    WinFormName : str
    FormImage : Optional[str] 
    ISWeb : Optional[str]
    IS_MO : Optional[int]
    IsActive  : str
    AddedBy : int 
    AddedOn : datetime
    class Config:
        orm_mode=True
        
     
class add(BaseModel):
    FormName : str
    ModuleCode : int
    SubModuleCode : int
    IndexNum : int
    WinFormName : str
    FormImage : Optional[str] 
    ISWeb : str
    IS_MO : int
    IsActive  : str
    
class update(BaseModel):
    FormName : str
    ModuleCode : int
    SubModuleCode : int
    IndexNum : int
    WinFormName : str
    FormImage : Optional[str] 
    ISWeb : str
    IS_MO : str
    IsActive  : str 
    
    
class postout(BaseModel):
    FormName : str
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    FormName : str
    code : str = "200"
    status : str = "Updated"