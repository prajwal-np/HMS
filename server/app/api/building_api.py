from schemas.user_schema import UserSchema, LoginUserModel, LoggedUser
from schemas.building_schema import InsertBuilding, BuildingSchema
from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from starlette.requests import Request
from utils.middleware import Middleware
from services.building_service import insert_building, get_building, update_building, delete_building, UpdateBuilding
from typing import Union

router = APIRouter(prefix='/building',tags=['Building'],dependencies=[Depends(Middleware)])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=BuildingSchema)
def create_building(request: Request, building: InsertBuilding):
    try:
        result = insert_building(request=request, building=building)
        return result
    except Exception as error:
        print(error)
        raise HTTPException(status_code=403,detail='Cannot perform the operation')

@router.get("/{id}", status_code=status.HTTP_201_CREATED, response_model=Union[UpdateBuilding, None])
def get_building_by_id(request: Request, id: int)->Union[UpdateBuilding, None]:
    try:
        result = get_building(request,id)
        return result
    except Exception as error:
        print(error)

@router.put("/", status_code=status.HTTP_201_CREATED, response_model=UpdateBuilding)
def update_building_api(request: Request, building: UpdateBuilding):
    try:
        result = update_building(request, building)
        return result
    except Exception as error:
        print(error)

@router.delete("/{id}", status_code=status.HTTP_201_CREATED, response_model=str)
def delete_building_api(request: Request, id: int):
    try:
        result = delete_building(request, id)
        return result
    except Exception as error:
        print(error)
