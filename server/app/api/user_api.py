from app.schemas.user_schema import UserSchema, InsertUser, LoginUserModel
from fastapi import APIRouter
from starlette import status
from starlette.requests import Request
from app.services.user_service import authenticate_user, register_user
router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserSchema)
def create_user(request: Request, user: InsertUser):
    print(user)
    return register_user(request=request, user=user)

@router.post("/login", status_code=status.HTTP_201_CREATED)
def login_user(request: Request, login_request: LoginUserModel):
   response = authenticate_user(request, email=login_request.email, password=login_request.password)
   return response
