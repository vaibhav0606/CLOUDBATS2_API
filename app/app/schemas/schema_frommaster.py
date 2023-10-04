from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional
from .schema_moduleMaster import showmodule
from .schema_subModuleMaster import showsubmodule


class show(BaseModel):
    FormCode : int 
    FormName : str
    module : showmodule
    SubModule : showsubmodule
    IndexNum : Optional[int]
    WinFormName : str
    FormImage : Optional[str] 
    IS_MO : Optional[int]
    IsActive  : int
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
    IS_MO : Optional[int] 
    IsActive  : int
    
class update(add):
   pass
    
class postout(BaseModel):
    FormName : str
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    FormName : str
    code : str = "200"
    status : str = "Updated"

class showform(BaseModel):
    FormCode : int 
    FormName : str