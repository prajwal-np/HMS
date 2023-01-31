from fastapi import FastAPI
from app.api.user_api import router
from app.config.db import session_maker
from app.data_access.repositories_registry import RepositoriesRegistry
from app.data_access.user.user_repository import UserRepository
def create_server():
    server = FastAPI(debug=True, title= 'HMSV0.0', version='0.0.1')
    server.include_router(router)
    server.session_maker = session_maker
    server.repositories = RepositoriesRegistry(user_repo=UserRepository)
    return server