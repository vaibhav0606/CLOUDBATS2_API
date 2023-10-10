from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional

class show(BaseModel):
    DepartmentCode : int
    DepartmentName : str
    ShortName : str
    IsActive  : int
    AddedBy : int 
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    DepartmentName : str
    ShortName : str
    IsActive  : int
    
class update(add):
   pass
    
class postout(BaseModel):
    DepartmentName : str
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    DepartmentName : str
    code : str = "200"
    status : str = "Updated"
    
class showdepartment(BaseModel):
    DepartmentCode : int
    DepartmentName : str

class loaddropdown(BaseModel):
    DepartmentCode : int
    DepartmentName : str
    class Config:
        orm_mode=True