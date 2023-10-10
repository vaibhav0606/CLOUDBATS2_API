from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional
from .schema_starcasttype import showstarcasttype
from app.schemas.admin.schema_countrymaster import showcountry

class show(BaseModel):
    StarCastCode : int
    StarCastName : str
    StarCastTypeMaster : showstarcasttype
    MaleFemale : str
    DateOfBirth : datetime 
    DateOfDeath : datetime
    StarCast_Image : str
    Country : showcountry
    IsActive  : int
    AddedBy : int 
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    StarCastName : str
    StarCastTypeCode : int
    MaleFemale : str
    DateOfBirth : datetime 
    DateOfDeath : datetime
    StarCast_Image : str
    CountryCode : int
    IsActive  : int
    
class update(BaseModel):
    pass 
    
class postout(BaseModel):
    StarCastName : str
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    StarCastName : str
    code : str = "200"
    status : str = "Updated"
    

class loaddropdown(BaseModel):
    StarCastCode : int
    StarCastName : str
    class Config:
        orm_mode=True
