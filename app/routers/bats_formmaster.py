from fastapi import APIRouter,Depends
from .. import database,oauth2,userschema
from app.schemas import schema_frommaster as schema
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends
from app.datacode import formmaster as datacode
from typing import List

router=APIRouter(prefix="/formmaster",tags=["Form Master"])

@router.get('/',response_model=List[schema.show])
def get_all(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):#current_user: userschema.User = Depends(oauth2.get_current_user)
    return datacode.get_all(db)

@router.get('/{FormCode}',response_model=schema.show)
def get_id(FormCode:int,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_id(FormCode,db)

@router.post('/', response_model=schema.postout)
def create(request: schema.add,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.create(request,db,current_user)

@router.put('/{FormCode}',  response_model=schema.putout)
def update(FormCode:int, request: schema.update, db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.update(FormCode,request, db,current_user)