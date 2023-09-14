from pydantic import BaseModel
from datetime import datetime,date



class showlocation(BaseModel):
    LocationCode : int
    LocationName : str
    ShortName : str
    CurrencyCode : int
    TimeZoneCode : str
    IsActive : str
    AddedBy : int
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class addLocation(BaseModel):
    LocationName : str
    ShortName : str
    CurrencyCode : int
    TimeZoneCode : str
    IsActive : str
    AddedBy : int
    
class updatelocation(BaseModel):
    LocationName : str
    ShortName : str
    CurrencyCode : int
    TimeZoneCode : str
    IsActive : str
    ModifiedBy : int
    ModifiedOn : datetime