from pydantic import BaseModel
from datetime import datetime
from .schema_channelmaster import showchannel
from .schema_locationmaster import showlocation
from .schema_entitymaster import showentity

class show(BaseModel):
    Id : int
    Entity : showentity  
    locations : showlocation
    Channel : showchannel
    AddedBy : int
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    EntityCode : int  
    LocationCode : int
    ChannelCode : int
    
class update(add):
   pass

class postout(BaseModel):
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    code : str = "200"
    status : str = "Updated"
    
