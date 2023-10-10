from pydantic import BaseModel
from datetime import datetime,date




class show(BaseModel):
    GenreCode : int
    GenreName : str
    IsActive : int
    AddedBy : int
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    GenreName : str
    IsActive : int

class update(add):
    pass

class postout(BaseModel):
    GenreName : str
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    GenreName : str
    code : str = "200"
    status : str = "Updated"
    
class showGenre(BaseModel):
    GenreCode : int
    GenreName : str

class loaddropdown(BaseModel):
    GenreCode : int
    GenreName : str
    class Config:
        orm_mode=True