
from sqlalchemy.orm import Session
from app.models import models_master
from app.schemas import schema_subgenreMaster
from fastapi import HTTPException,status
from datetime import datetime

def create(request:schema_subgenreMaster.add,db: Session,current_user):
    Check=db.query(models_master.SubGenreMaster).filter(models_master.SubGenreMaster.SubGenreName == request.SubGenreName)
    if Check.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"SubGenre is Already Exists")
    create=models_master.SubGenreMaster(AddedBy=current_user.LoginCode,**request.model_dump())
    #create=models_master.SubGenreMaster(ZoneName=request.ZoneName,ShortName=request.ShortName,IsActive=request.IsActive,AddedBy=request.AddedBy)
    db.add(create)
    db.commit()
    db.refresh(create)
    #return create 
    return create 

def update(SubGenreCode:int,request:schema_subgenreMaster.update,db: Session,current_user):
    update_query=db.query(models_master.SubGenreMaster).filter(models_master.SubGenreMaster.SubGenreCode == SubGenreCode)
    if not update_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"SubGenre not found")
    Check=db.query(models_master.SubGenreMaster).filter(models_master.SubGenreMaster.SubGenreName == request.SubGenreName,
                                                       models_master.SubGenreMaster.SubGenreCode != SubGenreCode)
    if Check.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"SubGenre is Already Exists")
    update_data = request.model_dump()
    update_data["ModifiedBy"] = current_user.LoginCode 
    update_data["ModifiedOn"] = datetime.utcnow() 
    update_query.update(update_data, synchronize_session=False)
    db.commit()
    return update_query.first()

def get_id(SubGenreCode:int,db:Session):
    user = db.query(models_master.SubGenreMaster).filter(models_master.SubGenreMaster.SubGenreCode == SubGenreCode).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"SubGenre not available")
    return user

def get_all(db:Session):
        get_all=db.query(models_master.SubGenreMaster).all()
        if not get_all:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data not found")
        return get_all
  
  


