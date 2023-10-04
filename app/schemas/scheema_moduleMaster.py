from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional
class show(BaseModel):
    ModuleCode : int 
    ModuleName : Optional[str]
    IndexNum :  Optional[int]
    ModuleImage : Optional[str]
    IsActive  : str
    AddedBy : int
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    ModuleName : str
    IndexNum : int
    ModuleImage : str
    IsActive  : str
    AddedBy : int 
    
class update(BaseModel):
    ModuleName : str
    IndexNum : int
    ModuleImage : str
    IsActive  : str 
    ModifiedBy : int
    
        
class showfrommodule(BaseModel):
    ModuleCode : int
    ModuleName : str
    class Config:
        orm_mode=True    

class showsubmodule(BaseModel):
    ModuleCode : int
    ModuleName : str
    class Config:
        orm_mode=True    