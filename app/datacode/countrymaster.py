
from sqlalchemy.orm import Session
from app.models import models_master
from app.schemas import schema_countrymaster
from fastapi import HTTPException,status
from datetime import datetime

def create(request:schema_countrymaster.add,db: Session,current_user):
    Check=db.query(models_master.CountryMaster).filter(models_master.CountryMaster.CountryName == request.CountryName)
    if Check.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Country is Already Exists")
    create=models_master.CountryMaster(AddedBy=current_user.LoginCode,**request.model_dump())
    db.add(create)
    db.commit()
    db.refresh(create)
    return create 

def update(CountryCode:int,request:schema_countrymaster.update,db: Session,current_user):
    update_query=db.query(models_master.CountryMaster).filter(models_master.CountryMaster.CountryCode == CountryCode)
    if not update_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Country  not found")
    Check=db.query(models_master.CountryMaster).filter(models_master.CountryMaster.CountryName == request.CountryName,
                                                       models_master.CountryMaster.CountryCode != CountryCode)
    if Check.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Country is Already Exists")
    update_data = request.model_dump()
    update_data["ModifiedBy"] = current_user.LoginCode 
    update_data["ModifiedOn"] = datetime.utcnow() 
    update_query.update(update_data, synchronize_session=False)
    db.commit()
    return update_query.first()

def get_id(CountryCode:int,db:Session):
    user = db.query(models_master.CountryMaster).filter(models_master.CountryMaster.CountryCode == CountryCode).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Country  not available")
    return user

def get_all(db:Session):
   
        get_all=db.query(models_master.CountryMaster).all()
        if not get_all:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data not found")
        return get_all
   
  


