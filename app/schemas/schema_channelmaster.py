from pydantic import BaseModel
from datetime import datetime,date

class showchannel(BaseModel):
    ChannelCode : int
    ChannelName : str
    ShortName : str
    Channel_Image : str
    ChannelGenre : str
    ChannelContentType : str
    IsActive :str
    AddedBy : int 
    AddedOn : datetime
    StateCode : int
    SACCode : str
    GSTN_id : str
    class Config:
        orm_mode=True
     
class addchannel(BaseModel):
    ChannelName : str
    ShortName : str
    Channel_Image : str
    ChannelGenre : str
    ChannelContentType : str
    IsActive :str
    AddedBy : int 
    StateCode : int
    SACCode : str
    GSTN_id : str
    
class updatechannel(BaseModel):
    ChannelName : str
    ShortName : str
    Channel_Image : str
    ChannelGenre : str
    ChannelContentType : str
    IsActive :str
    StateCode : int
    SACCode : str
    GSTN_id : str
    ModifiedBy : int
    ModifiedOn : datetime