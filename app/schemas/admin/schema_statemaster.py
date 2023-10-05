from pydantic import BaseModel
from datetime import datetime
from . import schema_countrymaster



class show(BaseModel):
    StateCode : int
    StateName : str
    StateShortName : str
    Country : schema_countrymaster.showcountry
    StateTinNo : str
    IsActive : int
    AddedBy : int
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    StateName : str
    StateShortName : str
    CountryCode : int
    StateTinNo : str
    IsActive : int
    
class update(add):
   pass

class postout(BaseModel):
    StateName : str
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    StateName : str
    code : str = "200"
    status : str = "Updated"
    
class showstate(BaseModel):
    StateCode : int
    StateName : str
