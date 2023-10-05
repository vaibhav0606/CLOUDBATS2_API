import logging
from sqlalchemy.orm import Session
from app.models.models_master import moduleMaster as model 
from app.schemas.admin import schema_moduleMaster as schema
from fastapi import HTTPException,status
from datetime import datetime
logging.basicConfig(filename='app.log', level=logging.ERROR)

def create(request:schema.add,db: Session,current_user):
    try:
        Check=db.query(model).filter(model.ModuleName == request.ModuleName)
        if Check.first():
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Module is Already Exists")
        create=model(AddedBy=current_user.LoginCode,**request.model_dump())
        #create=model(ModuleName=request.ModuleName,IndexNum=request.IndexNum,ModuleImage=request.ModuleImage,IsActive=request.IsActive,AddedBy=request.AddedBy)
        db.add(create)
        db.commit()
        db.refresh(create)
        return create 
    except Exception as e:
        logging.error(f"moduleMaster in create: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")

def update(ModuleCode:int,request:schema.update,db: Session,current_user):
    try:
        update_query=db.query(model).filter(model.ModuleCode == ModuleCode)
        if not update_query.first():
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Module  not found")
        Check=db.query(model).filter(model.ModuleName == request.ModuleName,
                                                        model.ModuleCode != ModuleCode)
        if Check.first():
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Module is Already Exists")
        update_data = request.model_dump()
        update_data["ModifiedBy"] = current_user.LoginCode 
        update_data["ModifiedOn"] = datetime.utcnow() 
        update_query.update(update_data, synchronize_session=False)
        db.commit()
        return update_query.first()
    except Exception as e:
        logging.error(f"moduleMaster in update: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")

def get_id(ModuleCode:int,db:Session):
    try:
        data = db.query(model).filter(model.ModuleCode == ModuleCode).first()
        if not data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Module  not available")
        return data
    except Exception as e:
        logging.error(f"moduleMaster in get_id: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")

def get_all(db:Session):
    try:
        get_all=db.query(model).all()
        if not get_all:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data not found")
        return get_all
    except Exception as e:
        logging.error(f"moduleMaster in get_all: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")
   
  


