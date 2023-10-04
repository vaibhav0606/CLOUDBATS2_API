from fastapi import APIRouter,HTTPException,Response,status,Depends
from .. import database,oauth2,userschema
from app.schemas import schema_loginrights as schema
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from app.datacode import rights as datacode
from typing import List

router=APIRouter(prefix="/rights",tags=["Login Rights "])

@router.get('/',response_model=List[schema.show])
def get_all(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):#current_user: userschema.User = Depends(oauth2.get_current_user)
    return datacode.get_all(db)

@router.get('/{id}',response_model=schema.show)
def get_id(id:int,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_id(id,db)

@router.post('/', response_model=schema.postout)
def create(request: schema.add,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.create(request,db,current_user)
