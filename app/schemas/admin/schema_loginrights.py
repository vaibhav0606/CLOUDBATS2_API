from pydantic import BaseModel
from datetime import datetime
from .schema_moduleMaster import showmodule 
from .schema_subModuleMaster import showsubmodule
from .schema_frommaster import showform
from .schema_loginmaster import showlogins



class show(BaseModel):
    Login : showlogins
    model : showmodule
    SubModule : showsubmodule
    Form : showform
    CanRead : int
    CanWrite : int
    AddedBy : int
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    LoginCode : int
    ModuleCode : int
    SubModuleCode : int
    FormCode : int
    CanRead : int
    CanWrite : int

class update(add):
   pass

class postout(BaseModel):
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    code : str = "200"
    status : str = "Updated"
    
