from pydantic import BaseModel
from datetime import datetime

class show(BaseModel):
    ChannelCode : int
    ChannelName : str
    ShortName : str
    Channel_Image : str
    ChannelGenre : str
    ChannelContentType : str
    IsActive :int
    AddedBy : int 
    AddedOn : datetime
    StateCode : int
    SACCode : str
    GSTN_id : str
    class Config:
        orm_mode=True
     
class add(BaseModel):
    ChannelName : str
    ShortName : str
    Channel_Image : str
    ChannelGenre : str
    ChannelContentType : str
    IsActive :int
    StateCode : int
    SACCode : str
    GSTN_id : str
    
class update(BaseModel):
    pass
    
class postout(BaseModel):
    ChannelName : str
    code : str = "200"
    status : str = "success"
    
class putout(BaseModel):
    ChannelName : str
    code : str = "200"
    status : str = "Updated"
    
class showchannel(BaseModel):
    ChannelCode : int
    ChannelName : str