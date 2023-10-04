from pydantic import BaseModel
from datetime import datetime,date



class show(BaseModel):
    LocationCode : int
    LocationName : str
    ShortName : str
    CurrencyCode : int
    TimeZoneCode : str
    IsActive : int
    AddedBy : int
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    LocationName : str
    ShortName : str
    CurrencyCode : int
    TimeZoneCode : str
    IsActive : int

class update(add):
    pass

class postout(BaseModel):
    LocationName : str
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    LocationName : str
    code : str = "200"
    status : str = "Updated"
    
class showlocation(BaseModel):
    LocationName : str
    ShortName : str