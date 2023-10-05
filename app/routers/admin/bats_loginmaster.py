from fastapi import APIRouter,HTTPException,Response,status,Depends
from app import database,oauth2,userschema 
from app.schemas.admin import schema_loginmaster
from app.models import models_User
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from app.datacode.admin import loginmaster
from app.utils import encryption
from typing import List
router=APIRouter(prefix="/loginmaster",tags=["login master"])

@router.get('/',response_model=List[schema_loginmaster.showLogins])
def get_all(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return loginmaster.get_all(db)


@router.get('/{LoginCode}',response_model=schema_loginmaster.showLogins)
def get_id(LoginCode:int,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return loginmaster.get_id(LoginCode,db)


@router.post('/', response_model=schema_loginmaster.addLogin)
def create(request: schema_loginmaster.addLogin,db: Session = Depends(database.Connect_db)):
    return loginmaster.create(request,db)

@router.put('/{LoginCode}', status_code=status.HTTP_202_ACCEPTED)
def update(LoginCode:int, request: schema_loginmaster.updatelogin, db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return loginmaster.update(LoginCode,request, db)
