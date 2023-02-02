from schemas.food_routine_schema import FoodRoutineSchema,InsertFoodRoutine, UpdateFoodRoutine
from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from starlette.requests import Request
from utils.middleware import Middleware
from services.food_routine_service import insert_food_routine, get_food_routine, delete_food_routine, update_food_routine

router = APIRouter(prefix='/food_routine', tags=['Food Routine'], dependencies=[Depends(Middleware)])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=FoodRoutineSchema)
def create_routine(request: Request, food_routine: InsertFoodRoutine):
    try:
        result = insert_food_routine(request, food_routine)
        return result
    except Exception as error:
        print(error)
        raise HTTPException(status_code=403,detail='Cannot register')

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=UpdateFoodRoutine)
def get_routine(request: Request, id: int):
    try:
        result = get_food_routine(request,id)
        return result
    except Exception as error:
        print(error)

@router.put("/", status_code=status.HTTP_200_OK, response_model=FoodRoutineSchema)
def update_routine(request: Request, food_routine: UpdateFoodRoutine):
    try:
        result = update_food_routine(request, food_routine)
        return result
    except Exception as error:
        print(error)

@router.delete("/{id}", status_code=status.HTTP_200_OK, response_model=str)
def delete_routine(request: Request, id: int):
    try:
        result = delete_food_routine(request,id)
        return result
    except Exception as error:
        print(error)
