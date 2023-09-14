from fastapi import APIRouter,HTTPException,Response,status,Depends
from .. import database,oauth2,userschema
from app.schemas import schema_currencymaster
from app.models import models_master
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from app.datacode import currencymaster
from typing import List

router=APIRouter(prefix="/currencymaster",tags=["currency_master"])

@router.get('/',response_model=List[schema_currencymaster.showcurrency])
def get_all(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return currencymaster.get_all(db)

@router.get('/{CurrencyCode}',response_model=schema_currencymaster.showcurrency,)
def get_id(CurrencyCode:int,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return currencymaster.get_id(CurrencyCode,db)

@router.post('/', response_model=schema_currencymaster.addcurrency)
def create_currency(request: schema_currencymaster.addcurrency,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return currencymaster.create(request,db)

@router.put('/{CurrencyCode}', status_code=status.HTTP_202_ACCEPTED)
def update(CurrencyCode:int, request: schema_currencymaster.updatecurrency, db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return currencymaster.update(CurrencyCode,request, db)