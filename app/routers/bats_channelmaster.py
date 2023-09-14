from fastapi import APIRouter,HTTPException,Response,status,Depends
from .. import database,oauth2,userschema
from app.schemas import schema_channelmaster
from app.models import models_master
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from app.datacode import channelmaster
from typing import List

router=APIRouter(prefix="/channelmaster",tags=["channel master"])

@router.get('/',response_model=List[schema_channelmaster.showchannel])
def get_all(db: Session = Depends(database.Connect_db)):#current_user: userschema.User = Depends(oauth2.get_current_user)
    return channelmaster.get_all(db)

@router.get('/{ChannelCode}',response_model=schema_channelmaster.showchannel)
def get_id(ChannelCode:int,db: Session = Depends(database.Connect_db)):
    return channelmaster.get_id(ChannelCode,db)

@router.post('/', response_model=schema_channelmaster.addchannel)
def create(request: schema_channelmaster.addchannel,db: Session = Depends(database.Connect_db)):
    return channelmaster.create(request,db)

@router.put('/{ChannelCode}', status_code=status.HTTP_202_ACCEPTED)
def update(ChannelCode:int, request: schema_channelmaster.updatechannel, db: Session = Depends(database.Connect_db)):
    return channelmaster.update(ChannelCode,request, db)