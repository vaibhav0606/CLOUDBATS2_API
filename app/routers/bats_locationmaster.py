from fastapi import APIRouter,HTTPException,Response,status,Depends
from .. import database,oauth2,userschema
from app.schemas import schema_locationmaster
from app.models import models_master
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from app.datacode import locationmaster
from typing import List

router=APIRouter(prefix="/locationmaster",tags=["location_master"])

@router.get('/',response_model=List[schema_locationmaster.showlocation])
def get_all(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return locationmaster.get_all(db)

@router.get('/{LocationCode}',response_model=schema_locationmaster.showlocation)
def get_id(LocationCode:int,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return locationmaster.get_id(LocationCode,db)

@router.post('/', response_model=schema_locationmaster.addLocation)
def create_location(request: schema_locationmaster.addLocation,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return locationmaster.create(request,db)

@router.put('/{LocationCode}', status_code=status.HTTP_202_ACCEPTED)
def update(LocationCode:int, request: schema_locationmaster.updatelocation, db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return locationmaster.update(LocationCode,request, db)