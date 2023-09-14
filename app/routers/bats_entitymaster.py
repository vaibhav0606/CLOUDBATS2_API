from fastapi import APIRouter,HTTPException,Response,status,Depends
from .. import database,oauth2,userschema
from app.schemas import schema_entitymaster
from app.models import models_master
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from app.datacode import entitymaster
from typing import List

router=APIRouter(prefix="/Entitymaster",tags=["Entity master"])

@router.get('/',response_model=List[schema_entitymaster.showentity])
def get_all(db: Session = Depends(database.Connect_db)):#current_user: userschema.User = Depends(oauth2.get_current_user)
    return entitymaster.get_all(db)

@router.get('/{EntityCode}',response_model=schema_entitymaster.showentity)
def get_id(EntityCode:int,db: Session = Depends(database.Connect_db)):
    return entitymaster.get_id(EntityCode,db)

@router.post('/', response_model=schema_entitymaster.addentity)
def create(request: schema_entitymaster.addentity,db: Session = Depends(database.Connect_db)):
    return entitymaster.create(request,db)

@router.put('/{EntityCode}', status_code=status.HTTP_202_ACCEPTED)
def update(EntityCode:int, request: schema_entitymaster.updateentity, db: Session = Depends(database.Connect_db)):
    return entitymaster.update(EntityCode,request, db)