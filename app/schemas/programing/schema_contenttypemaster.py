from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional

class show(BaseModel):
    ContentTypeCode: int
    ContentTypeName: str
    MultiPart: Optional[int] 
    EpisodeSpecific: Optional[int]
    LiveEvent: Optional[int]
    SportEvent: Optional[int]
    IsActive: int
    AddedBy: int
    AddedOn: datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    ContentTypeName: str
    MultiPart: Optional[int] 
    EpisodeSpecific: Optional[int]
    LiveEvent: Optional[int]
    SportEvent: Optional[int]
    IsActive: int
class update(add):
    pass

class postout(BaseModel):
    ContentTypeName : str
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    ContentTypeName : str
    code : str = "200"
    status : str = "Updated"
    
class showGenre(BaseModel):
    ContentTypeCode: int
    ContentTypeName: str 

class loaddropdown(BaseModel):
    ContentTypeCode: int
    ContentTypeName: str
    class Config:
        orm_mode=True
        
        
        
    class ContentTypeMaster(BaseModel):
        ContentTypeCode: int
    ContentTypeName: str
    MultiPart: int = None
    EpisodeSpecific: int = None
    LiveEvent: int = None
    SportEvent: int = None
    IsActive: int
    AddedBy: int
    AddedOn: datetime
    ModifiedBy: int = None
    ModifiedOn: datetime = None