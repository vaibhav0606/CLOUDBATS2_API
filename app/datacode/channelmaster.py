
from sqlalchemy.orm import Session
from app.models import models_master
from app.schemas import schema_channelmaster
from fastapi import HTTPException,status
from app.utils import encryption

    
def create(request:schema_channelmaster.addchannel,db: Session):
    create=models_master.ChannelMaster(ChannelName=request.ChannelName,ShortName=request.ShortName,Channel_Image=request.Channel_Image,ChannelGenre=request.ChannelGenre,ChannelContentType=request.ChannelContentType,IsActive=request.IsActive,AddedBy=request.AddedBy,StateCode=request.StateCode,SACCode=request.SACCode,GSTN_id=request.GSTN_id)
    db.add(create)
    db.commit()
    db.refresh(create)
    return create 

def update(ChannelCode:int,request:schema_channelmaster.updatechannel,db: Session):
    update=db.query(models_master.ChannelMaster).filter(models_master.ChannelMaster.ChannelCode == ChannelCode)
    if not update.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Entity with EntityCode {ChannelCode} not found")
    update=update.update(request)
    db.commit()
    db.refresh(update)
    return 'updated'

def get_id(ChannelCode:int,db:Session):
    data = db.query(models_master.ChannelMaster).filter(models_master.ChannelMaster.ChannelCode == ChannelCode).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Channel with the ChannelCode {ChannelCode} is not available")
    return data

def get_all(db:Session):
    get_all=db.query(models_master.ChannelMaster).all()
    if not get_all:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data not found")
    return get_all


