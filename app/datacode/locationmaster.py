
from sqlalchemy.orm import Session
from app.models import models_master
from app.schemas import schema_locationmaster
from fastapi import HTTPException,status
from app.utils import encryption


def create(request:schema_locationmaster.addLocation,db: Session):
    create=models_master.LocationMaster(LocationName=request.LocationName,ShortName=request.ShortName,CurrencyCode=request.CurrencyCode,TimeZoneCode=request.TimeZoneCode,IsActive=request.IsActive,AddedBy=request.AddedBy)
    db.add(create)
    db.commit()
    db.refresh(create)
    return create 

def update(LocationCode:int,request:schema_locationmaster.updatelocation,db: Session):
    update=db.query(models_master.LocationMaster).filter(models_master.LocationMaster.LocationCode == LocationCode)
    if not update.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Location with LocationCode {LocationCode} not found")
    update=update.update(request)
    db.commit()
    db.refresh(update)
    return 'updated'

def get_id(LocationCode:int,db:Session):
    user = db.query(models_master.LocationMaster).filter(models_master.LocationMaster.LocationCode == LocationCode).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Location with the LocationCode {LocationCode} is not available")
    return user

def get_all(db:Session):
    get_all=db.query(models_master.LocationMaster).all()
    if not get_all:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data not found")
    return get_all


