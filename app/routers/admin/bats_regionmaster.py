from fastapi import APIRouter,HTTPException,Response,status,Depends
from app import database,oauth2,userschema
from app.schemas.admin import schema_regionMaster as schema
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from app.datacode.admin import regionmaster as datacode
from typing import List

router=APIRouter(prefix="/regionmaster",tags=["Region Master"])

@router.get('/',response_model=List[schema.show])
def get_all(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_all(db)

@router.get('/{RegionCode}',response_model=schema.show)
def get_id(RegionCode:int,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_id(RegionCode,db)

@router.post('/', response_model=schema.postout)
def create(request: schema.add,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.create(request,db,current_user)

@router.put('/{RegionCode}', response_model=schema.putout)
def update(RegionCode:int, request: schema.update, db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.update(RegionCode,request, db,current_user)


@router.get('/drop/',response_model=List[schema.loaddropdown])
def get_drop(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_drop(db)