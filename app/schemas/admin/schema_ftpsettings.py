from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class show(BaseModel):
    FTPSettingCode : int
    SettingDesc : str
    FTPLocation : str
    FTP_UserID : Optional[str]
    FTP_PWD : Optional[str]
    FTP_Port : Optional[str]
    IsActive :int
    AddedBy : int 
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    SettingDesc : str
    FTPLocation : str
    FTP_UserID : Optional[str]
    FTP_PWD : Optional[str]
    FTP_Port : Optional[str]
    IsActive :int
    
class update(add):
   pass
    
class postout(BaseModel):

    code : str = "200"
    status : str = "success"

class putout(BaseModel):

    code : str = "200"
    status : str = "Updated"
    

class loaddropdown(BaseModel):
    FTPSettingCode : int
    SettingDesc : str
    class Config:
        orm_mode=True
    