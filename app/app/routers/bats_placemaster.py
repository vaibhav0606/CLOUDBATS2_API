from fastapi import APIRouter,HTTPException,Response,status,Depends
from .. import database,oauth2,userschema
from app.schemas import schema_palcemaster as schema
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from app.datacode import placemaster as datacode
from typing import List

router=APIRouter(prefix="/placemaster",tags=["Place Master"])

@router.get('/',response_model=List[schema.show])
def get_all(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):#current_user: userschema.User = Depends(oauth2.get_current_user)
    return datacode.get_all(db)

@router.get('/{PlaceCode}',response_model=schema.show)
def get_id(PlaceCode:int,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_id(PlaceCode,db)

@router.post('/', response_model=schema.postout)
def create(request: schema.add,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.create(request,db,current_user)

@router.put('/{PlaceCode}', response_model=schema.putout)
def update(PlaceCode:int, request: schema.update, db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.update(PlaceCode,request, db,current_user)