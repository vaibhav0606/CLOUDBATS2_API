from pydantic import BaseModel
from datetime import datetime
from .schema_palcemaster import showplace
from .schema_countrymaster import showcountry
from .schema_statemaster import showstate
from .schema_departmentMaster import showdepartment
from .schema_designationMaster import showdesignation
from .schema_regionMaster import showregion
from typing import Optional


class show(BaseModel):
    EmployeeCode : int
    Emp_FirstName: str
    Emp_LastName: str
    Emp_Code: Optional[str]
    Emp_Email: Optional[str]
    Emp_Addr1: Optional[str]
    Emp_Addr2: Optional[str]
    Place: showplace
    Country: showcountry
    State: showstate
    Emp_Contact1: str
    Emp_Contact2: Optional[str]
    Emp_Grade: str
    Emp_DOB: datetime
    Emp_DOJ: datetime
    Emp_DOL: Optional[datetime]
    Emp_BloodGroup: Optional[str]
    Emp_Image: Optional[str]
    Department : showdepartment
    Designation : showdesignation
    ReportingTo: Optional[int]
    Emp_Description: Optional[str]
    Region : showregion
    IsActive: int
    AddedOn : datetime
    AddedBy: int
    class Config:
        orm_mode = True


class add(BaseModel):
    Emp_FirstName: str
    Emp_LastName: str
    Emp_Code: Optional[str]
    Emp_Email: Optional[str]
    Emp_Addr1: Optional[str]
    Emp_Addr2: Optional[str]
    PlaceCode: int
    StateCode: int
    CountryCode: int
    Emp_Contact1: str
    Emp_Contact2: str
    Emp_Grade: str
    Emp_DOB: datetime
    Emp_DOJ: datetime
    Emp_DOL: Optional[datetime]
    Emp_BloodGroup: Optional[str]
    Emp_Image: Optional[str]
    Emp_Image: str
    DepartmentCode: int
    DesignationCode: int
    ReportingTo: Optional[int]
    Emp_Description: Optional[str]
    RegionCode: int
    IsActive: int
    

    
class update(add):
    pass


class postout(BaseModel):
    Emp_FirstName : str
    code : str = "200"
    status : str = "success"

class putout(BaseModel):
    Emp_FirstName : str
    code : str = "200"
    status : str = "Updated"
    
class showemp(BaseModel):
    EmployeeCode : int
    Emp_FirstName: str
    Emp_LastName: str
    

class loaddropdown(BaseModel):
    EmployeeCode : int
    Emp_FirstName: str
    class Config:
        orm_mode=True
   
