from fastapi import APIRouter,Depends
from app import database,oauth2,userschema
from app.schemas.admin import schema_ftpsettings as schema
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends
from app.datacode.admin import ftpsetting as datacode
from typing import List

router=APIRouter(prefix="/ftpsetting",tags=["FTP Setting"])

@router.get('/',response_model=List[schema.show])
def get_all(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_all(db)

@router.get('/{FTPSettingCode}',response_model=schema.show,)
def get_id(FTPSettingCode:int,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_id(FTPSettingCode,db)

@router.post('/', response_model=schema.postout)
def create_currency(request: schema.add,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.create(request,db,current_user)

@router.put('/{FTPSettingCode}', response_model=schema.putout)
def update(FTPSettingCode:int, request: schema.update, db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.update(FTPSettingCode,request,db,current_user)