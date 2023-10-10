from fastapi import APIRouter,HTTPException,Response,status,Depends
from app import database,oauth2,userschema
from app.schemas.admin import schema_timeZonemaster as schema
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from app.datacode.admin import timeZonemaster as datacode
from typing import List

router=APIRouter(prefix="/timeZonemaster",tags=["Time Zone Master"])

@router.get('/',response_model=List[schema.show])
def get_all(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):#current_user: userschema.User = Depends(oauth2.get_current_user)
    return datacode.get_all(db)

@router.get('/{TimeZoneCode}',response_model=schema.show)
def get_id(TimeZoneCode:int,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_id(TimeZoneCode,db)

@router.post('/', response_model=schema.postout)
def create(request: schema.add,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.create(request,db,current_user)

@router.put('/{TimeZoneCode}', response_model=schema.putout)
def update(TimeZoneCode:int, request: schema.update, db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.update(TimeZoneCode,request, db,current_user)


@router.get('/drop/',response_model=List[schema.loaddropdown])
def get_drop(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_drop(db)