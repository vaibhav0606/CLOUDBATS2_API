from pydantic import BaseModel
from datetime import datetime,date
from .schema_countrymaster import showcountry



class show(BaseModel):
    LanguageCode : int
    LanguageName : str
    Country : showcountry
    AddedBy : int
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    LanguageName : str
    CountryCode : str

class update(add):
    pass

class postout(BaseModel):
    LanguageName : str
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    LanguageName : str
    code : str = "200"
    status : str = "Updated"
    
class showlocation(BaseModel):
    LocationName : str
    ShortName : str