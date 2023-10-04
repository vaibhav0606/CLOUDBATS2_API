
from sqlalchemy.orm import Session
from app.models import models_master
from app.schemas import schema_zoneMaster
from fastapi import HTTPException,status
from datetime import datetime

def create(request:schema_zoneMaster.add,db: Session,current_user):
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

def update(ZoneCode:int,request:schema_zoneMaster.update,db: Session,current_user):
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

def get_id(ZoneCode:int,db:Session):
    user = db.query(models_master.ZoneMaster).filter(models_master.ZoneMaster.ZoneCode == ZoneCode).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Zone not available")
    return user

def get_all(db:Session):
        get_all=db.query(models_master.ZoneMaster).all()
        if not get_all:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data not found")
        return get_all
  
  


