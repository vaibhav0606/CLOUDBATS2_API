from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional

class show(BaseModel):
    SubGenreCode : int
    SubGenreName : str  
    IsActive  : int
    AddedBy : int 
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    SubGenreName : str    
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
    
