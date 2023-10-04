from fastapi import FastAPI 
from typing import Optional
from .models import models_User, models_master
from .database import engine
"""
from starlette.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError
from .exception_handlers import request_validation_exception_handler, http_exception_handler, unhandled_exception_handler
from .middleware import log_request_middleware
"""
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
    bats_playoutmaster,
    bats_channelsetting,
    bats_entitymapping,
    bats_ftpsetting,
    bats_starcasttype,
    bats_starcastmaster,
    bats_genrecode
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
    bats_playoutmaster.router,
    bats_channelsetting.router,
    bats_entitymapping.router,
    bats_ftpsetting.router,
    bats_starcasttype.router,
    bats_starcastmaster.router,
    bats_genrecode.router
    
]


bats = FastAPI( title="BATS",
    description= "Python based API")
"""
#custome Logger 
bats.middleware("http")(log_request_middleware)
bats.add_exception_handler(RequestValidationError, request_validation_exception_handler)
bats.add_exception_handler(HTTPException, http_exception_handler)
bats.add_exception_handler(Exception, unhandled_exception_handler)
"""

for router in routers:
    bats.include_router(router)
