
import logging
from sqlalchemy.orm import Session
from app.models.models_master import StateMaster as model
from app.schemas.admin import schema_statemaster as schema
from fastapi import HTTPException,status
from datetime import datetime
logging.basicConfig(filename='app.log', level=logging.ERROR)

def create(request:schema.add,db: Session,current_user):
    try:
        Check=db.query(model).filter(model.StateName == request.StateName)
        if Check.first():
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"State is Already Exists")
        create=model(AddedBy=current_user.LoginCode,**request.model_dump())
        db.add(create)
        db.commit()
        db.refresh(create)
        return create 
    except HTTPException as http_exception:
        raise http_exception
    except Exception as e:
        logging.error(f"statemaster in create: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")

def update(StateCode:int,request:schema.update,db: Session,current_user):
    try:
        update_query=db.query(model).filter(model.StateCode == StateCode)
        if not update_query.first():
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"State not found")
        Check=db.query(model).filter(model.StateName == request.StateName,
                                                        model.StateCode != StateCode)
        if Check.first():
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"State is Already Exists")
        update_data = request.model_dump()
        update_data["ModifiedBy"] = current_user.LoginCode 
        update_data["ModifiedOn"] = datetime.utcnow() 
        update_query.update(update_data, synchronize_session=False)
        db.commit()
        return update_query.first()
    except HTTPException as http_exception:
        raise http_exception
    except Exception as e:
        logging.error(f"statemaster in update: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")

def get_id(StateCode:int,db:Session):
    try:
        data = db.query(model).filter(model.StateCode == StateCode).first()
        if not data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"State  not available")
        return data
    except HTTPException as http_exception:
        raise http_exception
    except Exception as e:
        logging.error(f"statemaster in get_id: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")

def get_all(db:Session):
    try:
        get_all=db.query(model).all()
        if not get_all:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data not found")
        return get_all
    except HTTPException as http_exception:
        raise http_exception
    except Exception as e:
        logging.error(f"statemaster in get_all: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")
   
  


def get_drop(db:Session):
    try:
        get_all=db.query(model).all()
        if not get_all:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data not found")
        return get_all
    except HTTPException as http_exception:
        raise http_exception
    except Exception as e:
        logging.error(f"statemaster in get_drop: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")
