
import logging
from sqlalchemy.orm import Session
from app.models.models_master import RegionMaster as model 
from app.schemas.admin import schema_regionMaster as schema
from fastapi import HTTPException,status
from datetime import datetime
logging.basicConfig(filename='app.log', level=logging.ERROR)

def create(request:schema.add,db: Session,current_user):
    try:
        Check=db.query(model).filter(model.RegionName == request.RegionName)
        if Check.first():
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Region is Already Exists")
        create=model(AddedBy=current_user.LoginCode,**request.model_dump())
        #create=model(RegionName=request.RegionName,ShortName=request.ShortName,ZoneCode=request.ZoneCode,IsActive=request.IsActive,AddedBy=request.AddedBy)
        db.add(create)
        db.commit()
        db.refresh(create)
        return create 
    except Exception as e:
        logging.error(f"regionMaster in create: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")

def update(RegionCode:int,request:schema.update,db: Session,current_user):
    try:
        update_query=db.query(model).filter(model.RegionCode == RegionCode)
        if not update_query.first():
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Region not found")
        Check=db.query(model).filter(model.RegionName == request.RegionName,
                                                        model.RegionCode != RegionCode)
        if Check.first():
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Region is Already Exists")
        update_data = request.model_dump()
        update_data["ModifiedBy"] = current_user.LoginCode 
        update_data["ModifiedOn"] = datetime.utcnow() 
        update_query.update(update_data, synchronize_session=False)
        db.commit()
        return update_query.first()
    except Exception as e:
        logging.error(f"regionMaster in update: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")

def get_id(RegionCode:int,db:Session):
    try:
        data = db.query(model).filter(model.RegionCode == RegionCode).first()
        if not data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Region not available")
        return data
    except Exception as e:
            logging.error(f"regionMaster in get_id: {str(e)}")
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")

def get_all(db:Session):
    try:
    # Code to create a show instance
        get_all=db.query(model).all()
        if not get_all:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data not found")
        return get_all
    except Exception as e:
        logging.error(f"regionMaster in get_all: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")

  


