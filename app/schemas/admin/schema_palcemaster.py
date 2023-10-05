from pydantic import BaseModel
from datetime import datetime
from .schema_countrymaster import showcountry 
from .schema_zoneMaster import showzone
from .schema_statemaster import showstate



class show(BaseModel):
    PlaceCode : int
    PlaceName : str
    ShortName : str
    Zone : showzone
    State : showstate
    Country : showcountry
    IsActive : int
    AddedBy : int
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    PlaceName : str
    ShortName : str
    ZoneCode : int
    StateCode : int
    CountryCode : int
    IsActive : int

class update(add):
   pass

class postout(BaseModel):
    PlaceName : str
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    PlaceName : str
    code : str = "200"
    status : str = "Updated"
    
class showplace(BaseModel):
    PlaceCode : int
    PlaceName : str