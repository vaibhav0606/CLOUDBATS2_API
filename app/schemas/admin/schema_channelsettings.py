from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .schema_channelmaster import showchannel
from .schema_locationmaster import showlocation
from .schema_playoutmaster import showPlayout

class show(BaseModel):
    LocationCode: int
    ChannelCode: int
    ValidLicenseKey: Optional[str] = None
    StartTime: Optional[str] = None
    EndTime: str
    ReportPath: Optional[str] = None
    FramePerSec: Optional[str] = None
    IsPlayoutIntegrationFlag: Optional[str] = None
    PlayoutCode: Optional[int] = None
    IsTRAI_InventoryRule: Optional[int] = None
    IsEPGIntegrationFlag: Optional[int] = None
    IsMAMIntegrationFlag: Optional[int] = None
    IsSAPIntegrationFlag: Optional[int] = None
    IsTallyIntegrationFlag: Optional[int] = None
    IsBreakPatternAllowed: Optional[int] = None
    IsTapeCounterFlag: Optional[int] = None
    VideoPath1: Optional[str] = None
    VideoPath2: Optional[str] = None
    VideoPath3: Optional[str] = None
    VideoPath4: Optional[str] = None
    VideoPath5: Optional[str] = None
    VideoPath6: Optional[str] = None
    VideoPath7: Optional[str] = None
    VideoPath8: Optional[str] = None
    VideoPath9: Optional[str] = None
    VideoPath10: Optional[str] = None
    ProviderCode: Optional[str] = None
    SapWebService: Optional[str] = None
    TallyIntegrationPath: Optional[str] = None
    MamCode: Optional[str] = None
    SequenceNo: Optional[str] = None
    IsDiscountFlag: Optional[int] = None
    IsRateCardAllowed: Optional[int] = None
    SRModificationAllowed: Optional[int] = None
    IsDealApproval: Optional[int] = None
    PaperMedia: Optional[str] = None
    IsActive :int
    AddedBy : int 
    AddedOn : datetime
    class Config:
        orm_mode=True
     
class add(BaseModel):
    LocationCode: int
    ChannelCode: int
    ValidLicenseKey: Optional[str] = None
    StartTime: Optional[str] = None
    EndTime: str
    ReportPath: Optional[str] = None
    FramePerSec: Optional[str] = None
    IsPlayoutIntegrationFlag: Optional[str] = None
    PlayoutCode: int
    IsTRAI_InventoryRule: Optional[int] = None
    IsEPGIntegrationFlag: Optional[int] = None
    IsMAMIntegrationFlag: Optional[int] = None
    IsSAPIntegrationFlag: Optional[int] = None
    IsTallyIntegrationFlag: Optional[int] = None
    IsBreakPatternAllowed: Optional[int] = None
    IsTapeCounterFlag: Optional[int] = None
    VideoPath1: Optional[str] = None
    VideoPath2: Optional[str] = None
    VideoPath3: Optional[str] = None
    VideoPath4: Optional[str] = None
    VideoPath5: Optional[str] = None
    VideoPath6: Optional[str] = None
    VideoPath7: Optional[str] = None
    VideoPath8: Optional[str] = None
    VideoPath9: Optional[str] = None
    VideoPath10: Optional[str] = None
    ProviderCode: Optional[str] = None
    SapWebService: Optional[str] = None
    TallyIntegrationPath: Optional[str] = None
    MamCode: Optional[str] = None
    SequenceNo: Optional[str] = None
    IsDiscountFlag: Optional[int] = None
    IsRateCardAllowed: Optional[int] = None
    SRModificationAllowed: Optional[int] = None
    IsDealApproval: Optional[int] = None
    PaperMedia: Optional[str] = None
    IsActive: int
    
class update(BaseModel):
    pass
    
class postout(BaseModel):
    code : str = "200"
    status : str = "success"
    
class putout(BaseModel):
    code : str = "200"
    status : str = "Updated"
