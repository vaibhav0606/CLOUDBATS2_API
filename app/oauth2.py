from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from . import token
from .models import models_master
from . import database
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(data: str = Depends(oauth2_scheme),db: Session = Depends(database.Connect_db) ):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    tokendata=token.verify_token(data, credentials_exception)
    
    user = db.query(models_master.loginmaster).filter(models_master.loginmaster.LoginCode == tokendata.LoginCode).first()
    return user
