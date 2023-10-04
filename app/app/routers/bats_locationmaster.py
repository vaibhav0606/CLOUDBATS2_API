from fastapi import APIRouter,Depends
from .. import database,oauth2,userschema
from app.schemas import schema_locationmaster as schema
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends
from app.datacode import locationmaster as datacode
from typing import List

router=APIRouter(prefix="/locationmaster",tags=["Location_master"])

@router.get('/',response_model=List[schema.show])
def get_all(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_all(db)

@router.get('/{LocationCode}',response_model=schema.show)
def get_id(LocationCode:int,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_id(LocationCode,db)

@router.post('/', response_model=schema.postout)
def create_location(request: schema.add,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.create(request,db,current_user)

@router.put('/{LocationCode}', response_model=schema.putout)
def update(LocationCode:int, request: schema.update, db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.update(LocationCode,request, db,current_user)