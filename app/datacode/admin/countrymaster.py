import logging
from sqlalchemy.orm import Session
from app.models import models_master
from app.schemas.admin import schema_countrymaster
from fastapi import HTTPException,status
from datetime import datetime

logging.basicConfig(filename='app.log', level=logging.ERROR)

def create(request:schema_countrymaster.add,db: Session,current_user):
    try:
        Check=db.query(models_master.CountryMaster).filter(models_master.CountryMaster.CountryName == request.CountryName)
        if Check.first():
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Country is Already Exists")
        create=models_master.CountryMaster(AddedBy=current_user.LoginCode,**request.model_dump())
        db.add(create)
        db.commit()
        db.refresh(create)
        return create
    except Exception as e:
        logging.error(f"countrymaster in create: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")  

def update(CountryCode:int,request:schema_countrymaster.update,db: Session,current_user):
    try:
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
    except Exception as e:
        logging.error(f"countrymaster in update: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")

def get_id(CountryCode:int,db:Session):
    try:
        data = db.query(models_master.CountryMaster).filter(models_master.CountryMaster.CountryCode == CountryCode).first()
        if not data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Country  not available")
        return data
    except Exception as e:
        logging.error(f"countrymaster in get_id: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")

def get_all(db:Session):
    try:
        get_all=db.query(models_master.CountryMaster).all()
        if not get_all:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data not found")
        return get_all
    except Exception as e:
        logging.error(f"countrymaster in get_all: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")
    

def get_drop(db:Session):
    try:
        get_all=db.query(models_master.CountryMaster).all()
        if not get_all:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data not found")
        return get_all
    except HTTPException as http_exception:
        raise http_exception
    except Exception as e:
        logging.error(f"countrymaster in get_drop: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")
   
  


