from fastapi import FastAPI 
from typing import Optional
from app.routers import bats_user
from .models import models_User 
from .database import engine

models_User.Base.metadata.create_all(engine)



bats = FastAPI( title="BATS",
    description= "Python base API")

bats.include_router(bats_user.router)
