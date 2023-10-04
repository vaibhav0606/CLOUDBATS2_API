from pydantic import BaseModel
from datetime import datetime,date,Optional



class show(BaseModel):
    EmployeeCode = int
    Emp_FirstName: str
    Emp_LastName: str
    Emp_Code: str
    Emp_Email: str
    Emp_Addr1: str
    Emp_Addr2: str
    CityCode: int
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
    IsActive: str
    StateCode: int
    AddedOn : datetime
    AddedBy: int


class add(BaseModel):
    Emp_FirstName: str
    Emp_LastName: str
    Emp_Code: str
    Emp_Email: str
    Emp_Addr1: str
    Emp_Addr2: str
    CityCode: int
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
    IsActive: str
    StateCode: int
    AddedBy: int
    
class update(BaseModel):
    Emp_FirstName: str
    Emp_LastName: str
    Emp_Code: str
    Emp_Email: str
    Emp_Addr1: str
    Emp_Addr2: str
    CityCode: int
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
    IsActive: str
    StateCode: int
    ModifiedBy: int
    ModifiedOn: datetime
    
    class Config:
        orm_mode = True
