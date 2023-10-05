from fastapi import APIRouter,Depends
from app import database,oauth2,userschema
from app.schemas.admin import schema_languagemaster as schema
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends
from app.datacode.admin import languagemaster as datacode
from typing import List

router=APIRouter(prefix="/languagemaster",tags=["Language Master"])

@router.get('/',response_model=List[schema.show])
def get_all(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_all(db)

@router.get('/{LanguageCode}',response_model=schema.show)
def get_id(LanguageCode:int,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_id(LanguageCode,db)

@router.post('/', response_model=schema.postout)
def create_location(request: schema.add,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.create(request,db,current_user)

@router.put('/{LanguageCode}', response_model=schema.putout)
def update(LanguageCode:int, request: schema.update, db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.update(LanguageCode,request, db,current_user)