
from sqlalchemy.orm import Session
from app.models import models_master
from app.schemas import schema_currencymaster
from fastapi import HTTPException,status
from app.utils import encryption



def create(request:schema_currencymaster.addcurrency,db: Session):
    create=models_master.Currency(CurrencyName=request.CurrencyName,Currency_image=request.Currency_image,CurrencySymbol=request.CurrencySymbol,ShortName=request.ShortName,AddedBy=request.AddedBy)
    db.add(create)
    db.commit()
    db.refresh(create)
    return create 

def update(CurrencyCode:int,request:schema_currencymaster.updatecurrency,db: Session):
    update=db.query(models_master.Currency).filter(models_master.Currency.CurrencyCode == CurrencyCode)
    if not update.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"currency with CurrencyCode {CurrencyCode} not found")
    update=update.update(request)
    db.commit()
    db.refresh(update)
    return 'updated'

def get_id(CurrencyCode:int,db:Session):
    user = db.query(models_master.Currency).filter(models_master.Currency.CurrencyCode == CurrencyCode).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Currency with the CurrencyCode {CurrencyCode} is not available")
    return user

def get_all(db:Session):
    get_all=db.query(models_master.Currency).all()
    if not get_all:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data not found")
    return get_all


