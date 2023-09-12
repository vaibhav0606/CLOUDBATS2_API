from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas import schema_User
from .. import database  
from app.models import models_User 
from .. import token
from app.utils import encryption
from sqlalchemy.orm import Session
router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.Connect_db)):
    user = db.query(models_User.User).filter(models_User.User.Email == request.username ).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not encryption.encrypt.verify(user.Password, request.password ):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")

    access_token = token.create_access_token(data={"sub": user.Email})
    return {"access_token": access_token, "token_type": "bearer"}