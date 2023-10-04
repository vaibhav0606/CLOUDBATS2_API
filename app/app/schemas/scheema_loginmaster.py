from pydantic import BaseModel
from datetime import datetime,date


class showLogins(BaseModel):
    LoginCode : int
    LoginName : str
    Password : str
    EmployeeCode : int
    DefaultLocChnlCode : str
    RegisteredMobileNo : str
    MPIN: str
    TPIN: str
    IsFinalize: str
    IsActive : str
    IsAdmin : str
    SuperAdmin: str
    AddedBy : int
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class addLogin(BaseModel):
    LoginName : str
    Password : str
    EmployeeCode : int
    DefaultLocChnlCode : str
    RegisteredMobileNo : str
    MPIN: str
    TPIN: str
    IsFinalize: str
    IsActive : str
    IsAdmin : str
    SuperAdmin: str
    AddedBy : int
    
class updatelogin(BaseModel):
    LoginName : str
    Password : str
    EmployeeCode : int
    DefaultLocChnlCode : str
    RegisteredMobileNo : str
    MPIN: str
    TPIN: str
    IsFinalize: str
    IsActive : str
    IsAdmin : str
    SuperAdmin: str
    ModifiedBy : int
    ModifiedOn : datetime