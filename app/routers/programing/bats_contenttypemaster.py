from fastapi import APIRouter,Depends
from app import database,oauth2,userschema
from app.schemas.programing import schema_contenttypemaster as schema
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends
from app.datacode.programing import contenttypemaster as datacode
from typing import List

router=APIRouter(prefix="/contenttypemaster",tags=["Content type Master"])

@router.get('/',response_model=List[schema.show])
def get_all(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_all(db)

@router.get('/{ContentTypeCode}',response_model=schema.show)
def get_id(ContentTypeCode:int,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_id(ContentTypeCode,db)

@router.post('/', response_model=schema.postout)
def create_location(request: schema.add,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.create(request,db,current_user)

@router.put('/{ContentTypeCode}', response_model=schema.putout)
def update(ContentTypeCode:int, request: schema.update, db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.update(ContentTypeCode,request, db,current_user)

@router.get('/drop/',response_model=List[schema.loaddropdown])
def get_drop(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_drop(db)