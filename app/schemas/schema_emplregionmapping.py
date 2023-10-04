from pydantic import BaseModel
from datetime import datetime
from .schema_employeemaster import showemp
from .schema_regionMaster import showregion
from .schema_loginmaster import showlogins

class show(BaseModel):
    Employee : showemp  
    Region : showregion
    EffectiveFrom : datetime
    AddedBy : int
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    EmployeeCode : int
    RegionCode : int
    EffectiveFrom : datetime
    
class update(add):
   pass

class postout(BaseModel):
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    code : str = "200"
    status : str = "Updated"
    
