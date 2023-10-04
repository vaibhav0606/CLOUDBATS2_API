from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional

class show(BaseModel):
    DepartmentCode : int
    DepartmentName : str
    ShortName : str
    IsActive  : str
    AddedBy : int 
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    DepartmentName : str
    ShortName : str
    IsActive  : str
    
class update(BaseModel):
    DepartmentName : str
    ShortName : str
    IsActive  : str 
    
class postout(BaseModel):
    DepartmentName : str
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    DepartmentName : str
    code : str = "200"
    status : str = "Updated"