from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional
from .schema_starcasttype import showstarcasttype
from app.schemas.admin.schema_countrymaster import showcountry
from typing import Optional

class show(BaseModel):
    SubGenreCode: int
    SubGenreName: Optional[str]
    IsActive  : int
    AddedBy : int 
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    SubGenreName: str = None
    IsActive  : int
    
class update(add):
    pass 
    
class postout(BaseModel):
    SubGenreName : str
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    SubGenreName : str
    code : str = "200"
    status : str = "Updated"
    

class loaddropdown(BaseModel):
    SubGenreCode: int
    SubGenreName: str 
    class Config:
        orm_mode=True
