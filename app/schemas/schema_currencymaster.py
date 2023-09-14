from pydantic import BaseModel
from datetime import datetime,date



class showcurrency(BaseModel):
    CurrencyCode : int
    CurrencyName : str
    Currency_image : str
    CurrencySymbol : str
    ShortName : str
    AddedBy : int
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class addcurrency(BaseModel):
    CurrencyName : str
    Currency_image : str
    CurrencySymbol : str
    ShortName : str
    AddedBy : int
    
class updatecurrency(BaseModel):
    CurrencyName : str
    Currency_image : str
    CurrencySymbol : str
    ShortName : str
    ModifiedBy : int
    ModifiedOn : datetime