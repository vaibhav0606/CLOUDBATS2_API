from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional

class show(BaseModel):
    PlayoutCode : int
    PlayoutName : str
    PlaylistFileFormat : Optional[str]
    AsrunFileFormat : Optional[str]
    PlayoutLogo : Optional[str]
    IsActive  : int
    AddedBy : int 
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    PlayoutName : str
    PlaylistFileFormat : Optional[str]
    AsrunFileFormat : Optional[str]
    PlayoutLogo : Optional[str]
    IsActive  : int
    
class update(BaseModel):
    pass 
    
class postout(BaseModel):
    PlayoutName : str
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    PlayoutName : str
    code : str = "200"
    status : str = "Updated"
    
class showPlayout(BaseModel):
    PlayoutCode : int
    PlayoutName : str
    

class loaddropdown(BaseModel):
    PlayoutCode : int
    PlayoutName : str
    class Config:
        orm_mode=True