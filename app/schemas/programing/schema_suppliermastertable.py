from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from ..admin.schema_countrymaster import showcountry
from ..admin.schema_statemaster import showstate
from ..admin.schema_palcemaster import showplace

class show(BaseModel):
    SupplierCode: int
    SupplierName: str
    ShortName: str
    SupplierERPCode: Optional[str]
    Address1: str
    Address2: Optional[str]
    Pin: Optional[str]
    Country : showcountry 
    State: showstate
    Place: showplace
    Phone: Optional[str] 
    Mobile: Optional[str] 
    Fax: Optional[str] 
    Email: Optional[str] 
    ContactPerson: str
    IsActive: int
    AddedBy: int
    AddedOn: datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    SupplierName: str
    ShortName: str
    SupplierERPCode: Optional[str]
    Address1: str
    Address2: Optional[str]
    Pin: Optional[str]
    CountryCode: int
    StateCode : int
    PlaceCode: int
    Phone: Optional[str] 
    Mobile: Optional[str] 
    Fax: Optional[str] 
    Email: Optional[str] 
    ContactPerson: str
    IsActive: int
    
class update(add):
    pass 

class postout(BaseModel):
    SupplierName : str
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    SupplierName : str
    code : str = "200"
    status : str = "Updated"
    
class showsupplier(BaseModel):
    SupplierCode: int
    SupplierName: str

class loaddropdown(BaseModel):
    SupplierCode: int
    SupplierName: str
    class Config:
        orm_mode=True

