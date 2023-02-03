from schemas.user_schema import UserSchema, InsertUser, LoginUserModel, LoggedUser, RegisterUser
from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from starlette.requests import Request
from services.user_service import authenticate_user, register_user, get_user_by_email, on_board
from utils.middleware import Middleware

router = APIRouter(tags=['User'])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(request: Request, user: InsertUser):
    try:
        response = register_user(request=request, user=user)
        return response
    except Exception as error:
        print(error)
        raise HTTPException(status_code=403,detail='Cannot register')


@router.post("/login", status_code=status.HTTP_201_CREATED)
def login_user(request: Request, login_request: LoginUserModel):
    try:
        response = authenticate_user(request, email=login_request.email, password=login_request.password)
        if not response:
            raise HTTPException(status_code=403,detail='Cannot login')
        return response
    except Exception as error:
        print(error)


@router.get("/{email}", status_code=status.HTTP_200_OK, dependencies=[Depends(Middleware)])
def get_user_detail(request:Request, email: str)-> UserSchema:
    try:
        print(request.token)
        response = get_user_by_email(request, email)
        return response
    except Exception as e:
        print(e)
        raise HTTPException(status_code=403,detail='Cannot get user details')

@router.post("/onboard", status_code=status.HTTP_201_CREATED, dependencies=[Depends(Middleware)])
def on_board_api(request:Request, user: RegisterUser)-> str:
    try:
        response = on_board(request, user)
        # return response
        return 'asdasd'
    except Exception as e:
        print(e)
        raise HTTPException(status_code=403,detail='Cannot get user details')
        