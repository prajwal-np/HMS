from schemas.user_schema import UserSchema, InsertUser, LoginUserModel, LoggedUser
from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from starlette.requests import Request
from utils.middleware import Middleware
router = APIRouter(prefix='/routine',dependencies=[Depends(Middleware)], tags=['Food Routine'])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserSchema)
def create_routine(request: Request, user: InsertUser):
    try:
        pass
    except Exception as error:
        print(error)
        raise HTTPException(status_code=403,detail='Cannot register')

@router.get("/{id}", status_code=status.HTTP_201_CREATED, response_model=LoggedUser)
def get_routine(request: Request, id: str):
    try:
        pass
    except Exception as error:
        print(error)

@router.put("/", status_code=status.HTTP_201_CREATED, response_model=LoggedUser)
def update_routine(request: Request, login_request: LoginUserModel):
    try:
        pass
    except Exception as error:
        print(error)

@router.delete("/{id}", status_code=status.HTTP_201_CREATED, response_model=LoggedUser)
def delete_routine(request: Request, id: str):
    try:
        pass
    except Exception as error:
        print(error)