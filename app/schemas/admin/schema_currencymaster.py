from pydantic import BaseModel
from datetime import datetime,date



class show(BaseModel):
    CurrencyCode : int
    CurrencyName : str
    Currency_image : str
    CurrencySymbol : str
    ShortName : str
    AddedBy : int
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    CurrencyName : str
    Currency_image : str
    CurrencySymbol : str
    ShortName : str
    
class update(add):
    pass
    
class postout(BaseModel):
    CurrencyName : str
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    CurrencyName : str
    code : str = "200"
    status : str = "Updated"
    

class loaddropdown(BaseModel):
    CurrencyCode : int
    CurrencyName : str
    class Config:
        orm_mode=True