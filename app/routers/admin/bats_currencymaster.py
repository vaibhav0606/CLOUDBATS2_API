from fastapi import APIRouter,Depends
from app import database,oauth2,userschema
from app.schemas.admin import schema_currencymaster as schema
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends
from app.datacode.admin import currencymaster as datacode
from typing import List

router=APIRouter(prefix="/currencymaster",tags=["Currency Master"])

@router.get('/',response_model=List[schema.show])
def get_all(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_all(db)

@router.get('/{CurrencyCode}',response_model=schema.show,)
def get_id(CurrencyCode:int,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_id(CurrencyCode,db)

@router.post('/', response_model=schema.postout)
def create_currency(request: schema.add,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.create(request,db,current_user)

@router.put('/{CurrencyCode}', response_model=schema.putout)
def update(CurrencyCode:int, request: schema.update, db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.update(CurrencyCode,request,db,current_user)


@router.get('/drop/',response_model=List[schema.loaddropdown])
def get_drop(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_drop(db)