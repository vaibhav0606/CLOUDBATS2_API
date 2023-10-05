import logging
from sqlalchemy.orm import Session
from app.models import models_master
from app.schemas.admin import schema_zoneMaster
from fastapi import HTTPException,status
from datetime import datetime

logging.basicConfig(filename='app.log', level=logging.ERROR)

def create(request:schema_zoneMaster.add,db: Session,current_user):
    try:
        Check=db.query(models_master.ZoneMaster).filter(models_master.ZoneMaster.ZoneName == request.ZoneName)
        if Check.first():
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Zone is Already Exists")
        create=models_master.ZoneMaster(AddedBy=current_user.LoginCode,**request.model_dump())
        #create=models_master.ZoneMaster(ZoneName=request.ZoneName,ShortName=request.ShortName,IsActive=request.IsActive,AddedBy=request.AddedBy)
        db.add(create)
        db.commit()
        db.refresh(create)
        return create 
    except Exception as e:
        logging.error(f"zoneMaster in create: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error") 

def update(ZoneCode:int,request:schema_zoneMaster.update,db: Session,current_user):
    try:
        update_query=db.query(models_master.ZoneMaster).filter(models_master.ZoneMaster.ZoneCode == ZoneCode)
        if not update_query.first():
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Zone not found")
        Check=db.query(models_master.ZoneMaster).filter(models_master.ZoneMaster.ZoneName == request.ZoneName,
                                                        models_master.ZoneMaster.ZoneCode != ZoneCode)
        if Check.first():
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Zone is Already Exists")
        update_data = request.model_dump()
        update_data["ModifiedBy"] = current_user.LoginCode 
        update_data["ModifiedOn"] = datetime.utcnow() 
        update_query.update(update_data, synchronize_session=False)
        db.commit()
        return update_query.first()
    except Exception as e:
        logging.error(f"zoneMaster in update: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")

def get_id(ZoneCode:int,db:Session):
    try:
        data = db.query(models_master.ZoneMaster).filter(models_master.ZoneMaster.ZoneCode == ZoneCode).first()
        if not data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Zone not available")
        return data
    except Exception as e:
        logging.error(f"zoneMaster in get_id: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")

def get_all(db:Session):
    try:
        get_all=db.query(models_master.ZoneMaster).all()
        if not get_all:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data not found")
        return get_all
    except Exception as e:
        logging.error(f"zoneMaster in get_all: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")
  
  


