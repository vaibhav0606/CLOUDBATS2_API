from fastapi import APIRouter,HTTPException,Response,status,Depends
from .. import database,oauth2,userschema 
from app.schemas import scheema_loginmaster
from app.models import models_User
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from app.datacode import loginmaster
from app.utils import encryption
from typing import List
router=APIRouter(prefix="/loginmaster",tags=["login master"])

@router.get('/',response_model=List[scheema_loginmaster.showLogins])
def get_all(db: Session = Depends(database.Connect_db)):
    return loginmaster.get_all(db)


@router.get('/{LoginCode}',response_model=scheema_loginmaster.showLogins)
def get_id(LoginCode:int,db: Session = Depends(database.Connect_db)):
    return loginmaster.get_id(LoginCode,db)


@router.post('/', response_model=scheema_loginmaster.addLogin)
def create(request: scheema_loginmaster.addLogin,db: Session = Depends(database.Connect_db)):
    return loginmaster.create(request,db)

@router.put('/{LoginCode}', status_code=status.HTTP_202_ACCEPTED)
def update(LoginCode:int, request: scheema_loginmaster.updatelogin, db: Session = Depends(database.Connect_db)):
    return loginmaster.update(LoginCode,request, db)
