from pydantic import BaseModel
from datetime import datetime,date

class showentity(BaseModel):
    EntityCode : int
    EntityId : str
    EntityName : str
    PermAddress : str
    CorpAddress : str
    ContactPerson : str
    Contact : str
    IsActive :str
    AddedBy : int 
    AddedOn : datetime
    PANNO : str
    CINNumber : str
    class Config:
        orm_mode=True
     
class addentity(BaseModel):
    EntityId : str
    EntityName : str
    PermAddress : str
    CorpAddress : str
    ContactPerson : str
    Contact : str
    IsActive :str
    AddedBy : int 
    PANNO : str
    CINNumber : str
    
class updateentity(BaseModel):
    EntityId : str
    EntityName : str
    PermAddress : str
    CorpAddress : str
    ContactPerson : str
    Contact : str
    IsActive :str
    PANNO : str
    CINNumber : str
    ModifiedBy : int
    ModifiedOn : datetime