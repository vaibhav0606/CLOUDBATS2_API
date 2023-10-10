import logging
from sqlalchemy.orm import Session
from app.models.models_master import StarCastTypeMaster as model
from app.schemas.programing import schema_starcasttype as schema
from fastapi import HTTPException,status
from datetime import datetime
logging.basicConfig(filename='app.log', level=logging.ERROR)

def create(request:schema.add,db: Session,current_user):
    try:
        Check=db.query(model).filter(model.StarCastTypeName == request.StarCastTypeName)
        if Check.first():
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"star cast Type is Already Exists")
        create=model(AddedBy=current_user.LoginCode,**request.model_dump())
        db.add(create)
        db.commit()
        db.refresh(create)
        return create
    except HTTPException as http_exception:
        raise http_exception
    except Exception as e:
        # Log the exception
        logging.error(f"starcasttype in create: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")

def update(StarCastTypeCode:int,request:schema.update,db: Session,current_user):
    try:
        
        update_query=db.query(model).filter(model.StarCastTypeCode == StarCastTypeCode)
        if not update_query.first():
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"star cast Type is Already Exists")
        Check=db.query(model).filter(model.StarCastTypeName == request.StarCastTypeName,
                                                        model.StarCastTypeCode != StarCastTypeCode)
        if Check.first():
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"star cast Type is Already Exists")
        update_data = request.model_dump()
        update_data["ModifiedBy"] = current_user.LoginCode 
        update_data["ModifiedOn"] = datetime.utcnow() 
        update_query.update(update_data, synchronize_session=False)
        db.commit()
        return update_query.first()
    except HTTPException as http_exception:
        raise http_exception
    except Exception as e:
        # Log the exception
        logging.error(f"starcasttype in update: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")


def get_id(StarCastTypeCode:int,db:Session):
    try:
        user = db.query(model).filter(model.StarCastTypeCode == StarCastTypeCode).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"star cast Type is Already Exists")
        return user
    except HTTPException as http_exception:
        raise http_exception
    except Exception as e:
        # Log the exception
        logging.error(f"starcasttype in get_id: {str(e)}")
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
        # Log the exception
        logging.error(f"starcasttype in get_all: {str(e)}")
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
        logging.error(f"starcasttype in get_drop: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")
   
  


