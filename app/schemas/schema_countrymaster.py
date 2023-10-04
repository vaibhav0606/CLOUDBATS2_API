from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional

class show(BaseModel):
    CountryCode : int
    CountryName : str
    ShortName : str
    IsActive  : int
    AddedBy : int 
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    CountryName : str
    ShortName : str
    IsActive  : int
    
class update(BaseModel):
    CountryName : str
    ShortName : str
    IsActive  : int 
    
class postout(BaseModel):
    CountryName : str
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    CountryName : str
    code : str = "200"
    status : str = "Updated"
    
class showcountry(BaseModel):
    CountryCode : int
    CountryName : str

    