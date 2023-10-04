from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional

class show(BaseModel):
    DesignationCode : int
    DesignationName : str
    ShortName : str
    IsActive  : str
    AddedBy : int 
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    DesignationName : str
    ShortName : str
    IsActive  : str
    
class update(BaseModel):
    DesignationName : str
    ShortName : str
    IsActive  : str 
    
    
class postout(BaseModel):
    DesignationName : str
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    DesignationName : str
    code : str = "200"
    status : str = "Updated"