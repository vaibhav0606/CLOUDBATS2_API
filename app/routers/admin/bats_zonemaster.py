from fastapi import APIRouter,HTTPException,Response,status,Depends
from app import database,oauth2,userschema
from app.schemas.admin import schema_zoneMaster
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from app.datacode.admin import zonemaster
from typing import List

router=APIRouter(prefix="/zonemaster",tags=["Zone Master"])

@router.get('/',response_model=List[schema_zoneMaster.show])
def get_all(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):#current_user: userschema.User = Depends(oauth2.get_current_user)
    return zonemaster.get_all(db)

@router.get('/{ZoneCode}',response_model=schema_zoneMaster.show)
def get_id(ZoneCode:int,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return zonemaster.get_id(ZoneCode,db)

@router.post('/', response_model=schema_zoneMaster.postout)
def create(request: schema_zoneMaster.add,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return zonemaster.create(request,db,current_user)

@router.put('/{ZoneCode}', response_model=schema_zoneMaster.putout)
def update(ZoneCode:int, request: schema_zoneMaster.update, db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return zonemaster.update(ZoneCode,request, db,current_user)

@router.get('/drop/',response_model=List[schema_zoneMaster.loaddropdown])
def get_drop(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return zonemaster.get_drop(db)