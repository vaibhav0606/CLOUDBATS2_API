from fastapi import FastAPI 
from typing import Optional
from .models import models_User, models_master
from .database import engine
from fastapi.middleware.cors import CORSMiddleware
from app.routers import (
    bats_user,
    authentication,
    bats_currencymaster,
    bats_locationmaster,
    bats_loginmaster,
    bats_entitymaster,
    bats_channelmaster,
    bats_moduleMaster,
    bats_submodulemaster,
    bats_formmaster,
    bats_designationmaster,
    bats_departmentmaster,
    bats_zonemaster,
    bats_regionmaster,
    bats_countrymaster,
    bats_statemaster,
    bats_placemaster,
    bats_employeemaster,
    bats_loginrights,
    bats_loginlocchnlmapping,
    bats_regionmapping,
    bats_languagemaster,
    bats_timezonemaster,
    bats_eventcolormaster,
    bats_SubgenreMaster
)

models_User.Base.metadata.create_all(engine)
models_master.Base.metadata.create_all(engine)

routers = [
    authentication.router,
    bats_user.router,
    bats_loginmaster.router,
    bats_currencymaster.router,
    bats_locationmaster.router,
    bats_entitymaster.router,
    bats_channelmaster.router,
    bats_moduleMaster.router,
    bats_submodulemaster.router,
    bats_formmaster.router,
    bats_departmentmaster.router,
    bats_designationmaster.router,
    bats_zonemaster.router,
    bats_regionmaster.router,
    bats_countrymaster.router,
    bats_statemaster.router,
    bats_placemaster.router,
    bats_employeemaster.router,
    bats_loginrights.router,
    bats_loginlocchnlmapping.router,
    bats_regionmapping.router,
    bats_languagemaster.router,
    bats_timezonemaster.router,
    bats_eventcolormaster.router,
    bats_SubgenreMaster.router
    
]


bats = FastAPI( title="BATS",
    description= "Python based API")

for router in routers:
    bats.include_router(router)



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
