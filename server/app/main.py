from fastapi import FastAPI
import api.user_api as user_api
import api.building_api as building_api
import api.food_routine_api as routine_api
import api.tenant_api as tenant_api

from config.db import session_maker
from data_access.repositories_registry import RepositoriesRegistry
from data_access.user.user_repository import UserRepository
from data_access.building.building_repository import BuildingRepo
from data_access.food_routine.food_routine_repository import FoodRoutineRepo
from data_access.tenant.tenant_repository import TenantRepo


def create_server():
    server = FastAPI(debug=True, title= 'HMSV0.0', version='0.0.1')

    server.include_router(user_api.router)
    server.include_router(building_api.router)
    server.include_router(routine_api.router)
    server.include_router(tenant_api.router)

    server.session_maker = session_maker
    server.repositories = RepositoriesRegistry(
        user_repo=UserRepository, 
        building_repo=BuildingRepo,
        tenant_repo=TenantRepo, 
        food_routine_repo=FoodRoutineRepo)
    return server