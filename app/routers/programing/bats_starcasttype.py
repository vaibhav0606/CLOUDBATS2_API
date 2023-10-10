from fastapi import APIRouter,Depends
from app import database,oauth2,userschema
from app.schemas.programing import schema_starcasttype as schema
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends
from app.datacode.programing import starcasttype as datacode
from typing import List

router=APIRouter(prefix="/starcasttype",tags=["Star Cast Type"])

@router.get('/',response_model=List[schema.show])
def get_all(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):#current_user: userschema.User = Depends(oauth2.get_current_user)
    return datacode.get_all(db)

@router.get('/{StarCastTypeCode}',response_model=schema.show)
def get_id(StarCastTypeCode:int,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_id(StarCastTypeCode,db)

@router.post('/', response_model=schema.postout)
def create(request: schema.add,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.create(request,db,current_user)

@router.put('/{StarCastTypeCode}',  response_model=schema.putout)
def update(StarCastTypeCode:int, request: schema.update, db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.update(StarCastTypeCode,request, db,current_user)


@router.get('/drop/',response_model=List[schema.loaddropdown])
def get_drop(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_drop(db)