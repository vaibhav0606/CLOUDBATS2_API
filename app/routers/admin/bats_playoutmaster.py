from fastapi import APIRouter,Depends
from app import database,oauth2,userschema
from app.schemas.admin import schema_playoutmaster as schema
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends
from app.datacode.admin import playoutmaster as datacode
from typing import List

router=APIRouter(prefix="/playoutmaster",tags=["Playout Master "])

@router.get('/',response_model=List[schema.show])
def get_all(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):#current_user: userschema.User = Depends(oauth2.get_current_user)
    return datacode.get_all(db)

@router.get('/{PlayoutCode}',response_model=schema.show)
def get_id(PlayoutCode:int,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_id(PlayoutCode,db)

@router.post('/', response_model=schema.postout)
def create(request: schema.add,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.create(request,db,current_user)

@router.put('/{PlayoutCode}', response_model=schema.putout)
def update(PlayoutCode:int, request: schema.update, db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.update(PlayoutCode,request, db,current_user)