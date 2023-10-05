from pydantic import BaseModel
from datetime import datetime
from .schema_palcemaster import showplace
from .schema_countrymaster import showcountry
from .schema_statemaster import showstate
from .schema_departmentMaster import showdepartment
from .schema_designationMaster import showdesignation
from .schema_regionMaster import showregion


class show(BaseModel):
    EmployeeCode : int
    Emp_FirstName: str
    Emp_LastName: str
    Emp_Code: str
    Emp_Email: str
    Emp_Addr1: str
    Emp_Addr2: str
    Place: showplace
    Country: showcountry
    State: showstate
    Emp_Contact1: str
    Emp_Contact2: str
    Emp_Grade: str
    Emp_DOB: datetime
    Emp_DOJ: datetime
    Emp_DOL: datetime
    Emp_BloodGroup: str
    Emp_Image: str
    Department : showdepartment
    Designation : showdesignation
    ReportingTo: int
    Emp_Description: str
    Region : showregion
    IsActive: int
    AddedOn : datetime
    AddedBy: int
    class Config:
        orm_mode = True


class add(BaseModel):
    Emp_FirstName: str
    Emp_LastName: str
    Emp_Code: str
    Emp_Email: str
    Emp_Addr1: str
    Emp_Addr2: str
    CityCode: int
    StateCode: int
    CountryCode: int
    Emp_Contact1: str
    Emp_Contact2: str
    Emp_Grade: str
    Emp_DOB: datetime
    Emp_DOJ: datetime
    Emp_DOL: datetime
    Emp_BloodGroup: str
    Emp_Image: str
    DepartmentCode: int
    DesignationCode: int
    ReportingTo: int
    Emp_Description: str
    RegionCode: int
    IsActive: int
    

    
class update(BaseModel):
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
    
   
