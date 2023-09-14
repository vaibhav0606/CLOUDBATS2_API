import uuid
from sqlalchemy import Column, Integer, String, ForeignKey,Boolean
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime,BigInteger
from app.database import Base
from sqlalchemy.sql import func
from pydantic import BaseModel, Field
from sqlalchemy.orm import relationship

Base = declarative_base()

class Currency(Base):
    __tablename__ = 'tbl_CurrencyMaster'
    CurrencyCode = Column(BigInteger, primary_key=True, index=True ,autoincrement=True)
    CurrencyName = Column(String(50))
    Currency_image = Column(String)
    CurrencySymbol = Column(String(10))
    ShortName = Column(String(5))
    AddedBy = Column(BigInteger, nullable=False)
    AddedOn = Column(DateTime, default=func.now(), nullable=False)
    ModifiedBy = Column(BigInteger)
    ModifiedOn = Column(DateTime) 
    locations = relationship("LocationMaster", back_populates="currency")
    
class LocationMaster(Base):
    __tablename__ = 'tbl_LocationMaster' 
    LocationCode = Column(BigInteger, primary_key=True, index=True ,autoincrement=True)
    LocationName =Column(String)
    ShortName = Column(String)
    CurrencyCode = Column(BigInteger,ForeignKey('tbl_CurrencyMaster.CurrencyCode') )
    TimeZoneCode =Column(String)
    IsActive = Column(String,nullable=False)
    AddedBy = Column(BigInteger,nullable=False)
    AddedOn = Column(DateTime, default=func.now(), nullable=False)
    ModifiedBy = Column(BigInteger)
    ModifiedOn = Column(DateTime) 
    currency = relationship("Currency", back_populates="locations")

  
class EntityMaster(Base):
    __tablename__ = 'tbl_EntityMaster' 
    EntityCode = Column(BigInteger, primary_key=True, index=True ,autoincrement=True)
    EntityId =Column(String(10))
    EntityName = Column(String(100))
    PermAddress = Column(String(500)) 
    CorpAddress =Column(String(500))
    ContactPerson=Column(String(25))
    Contact=Column(String(100))
    IsActive = Column(String(1))
    AddedBy = Column(BigInteger,nullable=False)
    AddedOn = Column(DateTime, default=func.now(), nullable=False)
    ModifiedBy = Column(BigInteger)
    ModifiedOn = Column(DateTime) 
    PANNO = Column(String(50))
    ServiceTaxNo = Column(String(50))
    CINNumber = Column(String(50))

class ChannelMaster(Base):
    __tablename__ = 'tbl_ChannelMaster' 
    ChannelCode = Column(BigInteger, primary_key=True, index=True ,autoincrement=True)
    ChannelName =Column(String(10))
    ShortName = Column(String(10))
    Channel_Image = Column(String(100)) 
    ChannelGenre = Column(String(50))
    ChannelContentType = Column(String(50))
    IsActive = Column(String(1))
    AddedBy = Column(BigInteger,nullable=False)
    AddedOn = Column(DateTime, default=func.now(), nullable=False)
    ModifiedBy = Column(BigInteger)
    ModifiedOn = Column(DateTime) 
    StateCode = Column(BigInteger)
    SACCode = Column(String(50))
    GSTN_id = Column(String(50))


class EmployeeMaster(Base):
    __tablename__ = 'tbl_EmployeeMaster'

    EmployeeCode = Column(BigInteger, primary_key=True, autoincrement=True)
    Emp_FirstName = Column(String(50))
    Emp_LastName = Column(String(50))
    Emp_Code = Column(String(10))
    Emp_Email = Column(String(100))
    Emp_Addr1 = Column(String(100))
    Emp_Addr2 = Column(String(100))
    CityCode = Column(BigInteger)
    CountryCode = Column(BigInteger)
    Emp_Contact1 = Column(String(15))
    Emp_Contact2 = Column(String(15))
    Emp_Grade = Column(String(5))
    Emp_DOB = Column(DateTime)
    Emp_DOJ = Column(DateTime)
    Emp_DOL = Column(DateTime)
    Emp_BloodGroup = Column(String(10))
    Emp_Image = Column(String(500))
    DepartmentCode = Column(BigInteger)
    DesignationCode = Column(BigInteger)
    ReportingTo = Column(BigInteger)
    Emp_Description = Column(String(500))
    RegionCode = Column(BigInteger)
    IsActive = Column(String(1))
    AddedBy = Column(BigInteger, nullable=False)
    AddedOn = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    ModifiedBy = Column(BigInteger, nullable=True)
    ModifiedOn = Column(DateTime, server_default=func.current_timestamp(), onupdate=func.current_timestamp())
    StateCode = Column(BigInteger)

class RegionMaster(Base):
    __tablename__ = 'tbl_RegionMaster'

    RegionCode = Column(BigInteger, primary_key=True, autoincrement=True)
    RegionName = Column(String(50), nullable=False)
    ShortName = Column(String(10), nullable=False, default='W')
    ZoneCode = Column(String(10), nullable=False)
    IsActive = Column(String(1))
    AddedBy = Column(BigInteger, nullable=False)
    AddedOn = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    ModifiedBy = Column(BigInteger, nullable=True)
    ModifiedOn = Column(DateTime, server_default=func.current_timestamp(), onupdate=func.current_timestamp())    

class EmplRegionMapping(Base):
    __tablename__ = 'tbl_EmplRegionMapping'

    EmployeeCode = Column(BigInteger)
    OldRegionCode = Column(String(10))
    NewRegionCode = Column(String(10))
    EffectiveFrom = Column(DateTime)
    AddedBy = Column(BigInteger, nullable=False)
    AddedOn = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    ModifiedBy = Column(BigInteger, nullable=True)
    ModifiedOn = Column(DateTime, onupdate=func.current_timestamp())

class StateMaster(Base):
    __tablename__ = 'tbl_StateMaster'

    StateCode = Column(BigInteger, primary_key=True, autoincrement=True)
    StateName = Column(String(100))
    StateShortName = Column(String(10))
    IsActive = Column(CHAR(1))
    AddedBy = Column(BigInteger, nullable=False)
    AddedOn = Column(DateTime, server_default=func.current_timestamp())
    ModifiedBy = Column(BigInteger, nullable=True)
    ModifiedOn = Column(DateTime, server_default=func.current_timestamp(), onupdate=func.current_timestamp())
    StateTinNo = Column(String(5))
    CountryCode = Column(BigInteger)

class DesignationMaster(Base):
    __tablename__ = 'tbl_DesignationMaster'

    DesignationCode = Column(BigInteger, primary_key=True, autoincrement=True)
    DesignationName = Column(String(50), nullable=False)
    ShortName = Column(String(10), nullable=False)
    IsActive = Column(String(1))
    AddedBy = Column(BigInteger, nullable=False)
    AddedOn = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    ModifiedBy = Column(BigInteger, nullable=True)
    ModifiedOn = Column(DateTime, server_default=func.current_timestamp(), onupdate=func.current_timestamp())

class DepartmentMaster(Base):
    __tablename__ = 'tbl_DepartmentMaster'

    DepartmentCode = Column(BigInteger, primary_key=True, autoincrement=True)
    DepartmentName = Column(String(50), nullable=False)
    ShortName = Column(String(10), nullable=False)
    IsActive = Column(CHAR(1), nullable=False)
    AddedBy = Column(BigInteger, nullable=False)
    AddedOn = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    ModifiedBy = Column(BigInteger, nullable=True)
    ModifiedOn = Column(DateTime, server_default=func.current_timestamp(), onupdate=func.current_timestamp())    

class LoginLocChnlMapping(Base):
    __tablename__ = 'tbl_LoginLocChnlMapping'

    LoginCode = Column(BigInteger, primary_key=True, nullable=False)
    LocationCode = Column(BigInteger, primary_key=True, nullable=False)
    ChannelCode = Column(BigInteger, primary_key=True, nullable=False)
    AddedBy = Column(BigInteger, nullable=False)
    AddedOn = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    ModifiedBy = Column(BigInteger, nullable=True)
    ModifiedOn = Column(DateTime, server_default=func.current_timestamp(), onupdate=func.current_timestamp())

class LoginSelectedForms(Base):
    __tablename__ = 'tbl_LoginSelectedForms'

    LoginCode = Column(BigInteger)
    FormCode = Column(BigInteger, primary_key=True, nullable=False)
    PriorityCount = Column(Integer)    

class LoginGroup(Base):
    __tablename__ = 'tbl_LoginGroup'

    GroupCode = Column(BigInteger, primary_key=True, autoincrement=True)
    GroupName = Column(String(50), nullable=False)
    AddedBy = Column(BigInteger, nullable=False)
    AddedOn = Column(DateTime, server_default=func.current_timestamp())
    ModifiedBy = Column(BigInteger, nullable=True)
    ModifiedOn = Column(DateTime, server_default=func.current_timestamp(), onupdate=func.current_timestamp())

class LoginGroupForms(Base):
    __tablename__ = 'tbl_LoginGroupForms'

    GroupCode = Column(BigInteger, primary_key=True, nullable=False)
    FormCode = Column(BigInteger, primary_key=True, nullable=False)
    ModuleCode = Column(BigInteger, primary_key=True, nullable=False)
    SubModuleCode = Column(BigInteger, primary_key=True, nullable=False)
    CanRead = Column(String(10))
    CanWrite = Column(String(10))
    ModifiedBy = Column(BigInteger, nullable=True)
    ModifiedOn = Column(DateTime, server_default=func.current_timestamp())


class EventColorMaster(Base):
    __tablename__ = 'tbl_EventColorMaster'

    EventCode = Column(BigInteger, primary_key=True, autoincrement=True)
    EventName = Column(String(50), nullable=False)
    EventType = Column(String(50), nullable=False)
    EventDefaultFrontColor = Column(CHAR(12), nullable=False)
    EventDefaultBackColor = Column(CHAR(12), nullable=False)
    IsActive = Column(String(1))
    AddedBy = Column(BigInteger, nullable=False)
    AddedOn = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    ModifiedBy = Column(BigInteger, nullable=True)
    ModifiedOn = Column(DateTime, server_default=func.current_timestamp(), onupdate=func.current_timestamp())


class LoginEventColorMaster(Base):
    __tablename__ = 'tbl_LoginEventColorMaster'

    LoginCode = Column(BigInteger, primary_key=True, nullable=False)
    LocationCode = Column(BigInteger, primary_key=True, nullable=False)
    ChannelCode = Column(BigInteger, primary_key=True, nullable=False)
    EventCode = Column(BigInteger, primary_key=True, autoincrement=True)
    EventFrontColor = Column(String(100))
    EventBackColor = Column(String(100))
    AddedBy = Column(BigInteger, nullable=False)
    AddedOn = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    ModifiedBy = Column(BigInteger, nullable=True)
    ModifiedOn = Column(DateTime, server_default=func.current_timestamp(), onupdate=func.current_timestamp())


class LoginEventColorMaster(Base):
    __tablename__ = 'tbl_LoginEventColorMaster'

    LoginCode = Column(BigInteger, primary_key=True, nullable=False)
    LocationCode = Column(BigInteger, primary_key=True, nullable=False)
    ChannelCode = Column(BigInteger, primary_key=True, nullable=False)
    EventCode = Column(BigInteger, primary_key=True, autoincrement=True)
    EventFrontColor = Column(String(100))
    EventBackColor = Column(String(100))
    AddedBy = Column(BigInteger, nullable=False)
    AddedOn = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    ModifiedBy = Column(BigInteger, nullable=True)
    ModifiedOn = Column(DateTime, server_default=func.current_timestamp(), onupdate=func.current_timestamp())

class LanguageMaster(Base):
    __tablename__ = 'tbl_LanguageMaster'

    LanguageCode = Column(BigInteger, primary_key=True, autoincrement=True)
    LanguageName = Column(String(50), nullable=False)
    CountryCode = Column(String(10), nullable=False)
    AddedBy = Column(BigInteger, nullable=False)
    AddedOn = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    ModifiedBy = Column(BigInteger, nullable=True)
    ModifiedOn = Column(DateTime, server_default=func.current_timestamp(), onupdate=func.current_timestamp())


class PlaceMaster(Base):
    __tablename__ = 'tbl_PlaceMaster'

    PlaceCode = Column(BigInteger, primary_key=True, autoincrement=True)
    PlaceName = Column(String(50), nullable=False)
    ShortName = Column(String(10), nullable=False)
    PlaceTypeCode = Column(BigInteger, nullable=False)
    ZoneCode = Column(BigInteger)
    IsActive = Column(String(1), nullable=False)
    AddedBy = Column(BigInteger, nullable=False)
    AddedOn = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    ModifiedBy = Column(BigInteger, nullable=False)
    ModifiedOn = Column(DateTime, server_default=func.current_timestamp(), onupdate=func.current_timestamp())
    CountryCode = Column(BigInteger)
    StateCode = Column(BigInteger)


class PlaceTypeMaster(Base):
    __tablename__ = 'tbl_PlaceTypeMaster'

    PlaceTypeCode = Column(BigInteger, primary_key=True, autoincrement=True)
    PlaceTypeName = Column(String(40), nullable=False)
    IsActive = Column(String(1), nullable=False)
    AddedBy = Column(BigInteger, nullable=False)
    AddedOn = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    ModifiedBy = Column(BigInteger, nullable=False)
    ModifiedOn = Column(DateTime, server_default=func.current_timestamp(), onupdate=func.current_timestamp())

class ZoneMaster(Base):
    __tablename__ = 'tbl_ZoneMaster'

    ZoneCode = Column(BigInteger, primary_key=True, autoincrement=True)
    ZoneName = Column(String(50), nullable=False)
    ShortName = Column(String(10), nullable=False, default='W')
    IsActive = Column(String(1), nullable=False)
    AddedBy = Column(BigInteger, nullable=False)
    AddedOn = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    ModifiedBy = Column(BigInteger, nullable=True)
    ModifiedOn = Column(DateTime, server_default=func.current_timestamp(), onupdate=func.current_timestamp())

class EmailSettings(Base):
    __tablename__ = 'tbl_EmailSettings'

    MailSettingCode = Column(BigInteger, primary_key=True, autoincrement=True)
    SettingDesc = Column(String(100))
    SMTP_Server = Column(String(50))
    Sender_Email = Column(String(100))
    Sender_Pwd = Column(String(20))
    SMTP_Port = Column(Integer)
    IsActive = Column(String(1), nullable=False)
    AddedBy = Column(BigInteger, nullable=False)
    AddedOn = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    ModifiedBy = Column(BigInteger, nullable=True)
    ModifiedOn = Column(DateTime, server_default=func.current_timestamp(), onupdate=func.current_timestamp())


class EmailGroupMaster(Base):
    __tablename__ = 'tbl_EmailGroupMaster'

    LocationCode = Column(BigInteger, nullable=False)
    ChannelCode = Column(BigInteger, nullable=False)
    EmailGroupCode = Column(BigInteger, primary_key=True, autoincrement=True)
    EmailGroupName = Column(String(100), nullable=False)
    IsActive = Column(String(1), nullable=False)
    AddedBy = Column(BigInteger, nullable=False)
    AddedOn = Column(DateTime, nullable=True, server_default=func.current_timestamp())
    ModifiedBy = Column(BigInteger, nullable=True)
    ModifiedOn = Column(DateTime, nullable=True, server_default=func.current_timestamp(), onupdate=func.current_timestamp())

class EmailGroupDetail(Base):
    __tablename__ = 'tbl_EmailGroupDetail'

    EmailGroupCode = Column(BigInteger, nullable=False, primary_key=True)
    Email_ID = Column(String(60), nullable=False)
    DetailID = Column(BigInteger, primary_key=True, autoincrement=True)

class FTPSettings(Base):
    __tablename__ = 'tbl_FTPSettings'

    FTPSettingCode = Column(BigInteger, primary_key=True, autoincrement=True)
    SettingDesc = Column(String(100), nullable=True)
    FTPLocation = Column(String(50), nullable=True)
    FTP_UserID = Column(String(20), nullable=True)
    FTP_PWD = Column(String(20), nullable=True)
    FTP_Port = Column(Integer, nullable=True)
    IsActive = Column(String(1), nullable=False)
    AddedBy = Column(BigInteger, nullable=False)
    AddedOn = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    ModifiedBy = Column(BigInteger, nullable=True)
    ModifiedOn = Column(DateTime, nullable=True, server_default=func.current_timestamp(), onupdate=func.current_timestamp())


class KeyDateAlerts(Base):
    __tablename__ = 'tbl_keyDateAlerts'

    KeyAlertCode = Column(Integer, primary_key=True, autoincrement=True)
    KeyAlertName = Column(String(100), nullable=True)
    KeyAlertSpeciality = Column(String(100), nullable=True)
    KeyAlertPriority = Column(String(20), nullable=True)
    KeyAlertDate = Column(DateTime, nullable=True)
    KeyAlertRepeatType = Column(String(20), nullable=True)
    AlertBeforeInDays = Column(Integer, nullable=True)
    IsActive = Column(String(1), nullable=False)
    AddedBy = Column(Integer, nullable=False)
    AddedOn = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    ModifiedBy = Column(Integer, nullable=True)
    ModifiedOn = Column(DateTime, nullable=True, server_default=func.current_timestamp(), onupdate=func.current_timestamp())

class FormsMaster(Base):
    __tablename__ = 'tbl_FormsMaster'

    FormCode = Column(BigInteger, primary_key=True, autoincrement=True)
    FormName = Column(String(50), nullable=True)
    ModuleCode = Column(Integer, nullable=True)
    SubModuleCode = Column(Integer, nullable=True)
    IndexNum = Column(Integer, nullable=True)
    WinFormName = Column(String(2000), nullable=True)
    FormImage = Column(String(2000), nullable=True)
    IsActive = Column(String(1), nullable=False)
    AddedBy = Column(Integer, nullable=False)
    AddedOn = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    ModifiedBy = Column(Integer, nullable=True)
    ModifiedOn = Column(DateTime, nullable=True, server_default=func.current_timestamp(), onupdate=func.current_timestamp())
    ISWeb = Column(String(1), nullable=True)
    IS_MO = Column(Integer, nullable=True)

class ModuleMaster(Base):
    __tablename__ = 'tbl_ModuleMaster'

    ModuleCode = Column(BigInteger, primary_key=True, autoincrement=True)
    ModuleName = Column(String(50), nullable=True)
    IndexNum = Column(Numeric(precision=2, scale=0), nullable=True)
    ModuleImage = Column(Image, nullable=True)
    IsActive = Column(String(1), nullable=False)
    AddedBy = Column(Integer, nullable=False)
    AddedOn = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    ModifiedBy = Column(Integer, nullable=True)
    ModifiedOn = Column(DateTime, nullable=True, server_default=func.current_timestamp(), onupdate=func.current_timestamp())

class SubModuleMaster(Base):
    __tablename__ = 'tbl_SubModuleMaster'

    SubModuleCode = Column(BigInteger, primary_key=True, autoincrement=True)
    SubModuleName = Column(String(50), nullable=True)
    IndexNum = Column(Integer, nullable=True)
    ModuleCode = Column(Integer, nullable=True)
    SubModuleImage = Column(String(500), nullable=True)
    IsActive = Column(String(1), nullable=False)
    AddedBy = Column(Integer, nullable=False)
    AddedOn = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    ModifiedBy = Column(Integer, nullable=True)
    ModifiedOn = Column(DateTime, nullable=True, server_default=func.current_timestamp(), onupdate=func.current_timestamp())


class PlatformTypeMaster(Base):
    __tablename__ = 'tbl_PlatformTypeMaster'

    PlatformTypeCode = Column(Integer, primary_key=True, autoincrement=True)
    PlatformTypeName = Column(String(50), nullable=True)
    AddedBy = Column(Integer, nullable=False)
    AddedOn = Column(DateTime, nullable=True, server_default=func.current_timestamp())
    ModifiedBy = Column(Integer, nullable=True)
    ModifiedOn = Column(DateTime, nullable=True, server_default=func.current_timestamp(), onupdate=func.current_timestamp())

class MamMaster(Base):
    __tablename__ = 'tbl_MamMaster'

    MamCode = Column(BigInteger, primary_key=True, autoincrement=True)
    MAMFileFormat = Column(String(100), nullable=True)
    ShortName = Column(String(10), nullable=True)
    IsActive = Column(String(1), nullable=True)
    AddedBy = Column(Integer, nullable=False)
    AddedOn = Column(DateTime, nullable=True, server_default=func.current_timestamp())
    ModifiedBy = Column(Integer, nullable=True)
    ModifiedOn = Column(DateTime, nullable=True, server_default=func.current_timestamp(), onupdate=func.current_timestamp())
    MamName = Column(String(50), nullable=True)

class YearMaster(Base):
    __tablename__ = 'tbl_YearMaster'

    Yearcode = Column(BigInteger, primary_key=True, autoincrement=True)
    Description = Column(String(40), nullable=False)
    Startdate = Column(DateTime, nullable=False)
    EndDate = Column(DateTime, nullable=False)
    AddedBy = Column(Integer, nullable=False)
    AddedOn = Column(DateTime, nullable=True)
    LastModifyBy = Column(Integer, nullable=False)
    LastModifyOn = Column(DateTime, nullable=True)
    IsActive = Column(String(10), nullable=True)