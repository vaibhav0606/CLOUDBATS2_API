from fastapi import APIRouter,HTTPException,Response,status,Depends
from app import database,oauth2,userschema
from app.schemas.admin import schema_countrymaster
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from app.datacode.admin import countrymaster
from typing import List

router=APIRouter(prefix="/countrymaster",tags=["Country Master"])

@router.get('/',response_model=List[schema_countrymaster.show])
def get_all(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):#current_user: userschema.User = Depends(oauth2.get_current_user)
    return countrymaster.get_all(db)

@router.get('/{CountryCode}',response_model=schema_countrymaster.show)
def get_id(ModuleCode:int,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return countrymaster.get_id(ModuleCode,db)

@router.post('/', response_model=schema_countrymaster.postout)
def create(request: schema_countrymaster.add,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return countrymaster.create(request,db,current_user)

@router.put('/{CountryCode}', response_model=schema_countrymaster.putout)
def update(CountryCode:int, request: schema_countrymaster.update, db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return countrymaster.update(CountryCode,request, db,current_user)