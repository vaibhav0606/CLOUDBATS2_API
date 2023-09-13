from fastapi import FastAPI 
from typing import Optional
from app.routers import bats_user,authentication
from .models import models_User 
from .database import engine
from fastapi.middleware.cors import CORSMiddleware

models_User.Base.metadata.create_all(engine)



bats = FastAPI( title="BATS",description= "Python base FASTAPI")
bats.include_router(authentication.router)
bats.include_router(bats_user.router)


origins = [
    "*",  # Allow requests from this domain
    ]
bats.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # Allow cookies in CORS requests
    allow_methods=["*"],     # Allow all HTTP methods (you can specify a list of methods)
    allow_headers=["*"],     # Allow all HTTP headers (you can specify a list of headers)
)