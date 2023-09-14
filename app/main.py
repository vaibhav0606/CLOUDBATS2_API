from fastapi import FastAPI 
from typing import Optional
from app.routers import bats_user,authentication,bats_currencymaster,bats_locationmaster,bats_loginmaster
from .models import models_User, models_master,model_loginmaster
from .database import engine

models_User.Base.metadata.create_all(engine)
model_loginmaster.Base.metadata.create_all(engine)
models_master.Base.metadata.create_all(engine)


bats = FastAPI( title="BATS",
    description= "Python base API")
bats.include_router(authentication.router)
bats.include_router(bats_user.router)
bats.include_router(bats_loginmaster.router)
bats.include_router(bats_currencymaster.router)
bats.include_router(bats_locationmaster.router)



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