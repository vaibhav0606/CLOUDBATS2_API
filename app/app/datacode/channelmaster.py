
from sqlalchemy.orm import Session
from app.models.models_master import ChannelMaster as model
from app.schemas import schema_channelmaster  as schema
from fastapi import HTTPException,status
from datetime import datetime

    
def create(request:schema.add,db: Session,current_user):
    Check=db.query(model).filter(model.ChannelName == request.ChannelName)
    if Check.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"ChannelName is Already Exists")
    create=model(AddedBy=current_user.LoginCode,**request.dict())
    db.add(create)
    db.commit()
    db.refresh(create)
    return create 

def update(ChannelCode:int,request:schema.update,db: Session,current_user):
    
    update_query=db.query(model).filter(model.ChannelCode == ChannelCode)
    if not update_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Channel not found")
    Check=db.query(model).filter(model.ChannelName == request.ChannelName,
                                                       model.ChannelCode != ChannelCode)
    if Check.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"ChannelName is Already Exists")
    
    update_data = request.dict()
    update_data["ModifiedBy"] = current_user.LoginCode 
    update_data["ModifiedOn"] = datetime.utcnow() 
    update_query.update(update_data, synchronize_session=False)
    db.commit()
    return update_query.first()

def get_id(ChannelCode:int,db:Session):
    data = db.query(model).filter(model.ChannelCode == ChannelCode).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Channel not available")
    return data


def get_all(db:Session):
    get_all=db.query(model).all()
    if not get_all:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data not found")
    return get_all


