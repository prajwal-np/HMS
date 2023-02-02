from fastapi import Request
from schemas.food_routine_schema import InsertFoodRoutine, UpdateFoodRoutine, FoodRoutineSchema
from sqlalchemy.orm import Session
from data_access.food_routine.food_routine_repository import FoodRoutineRepo
def insert_food_routine(request:Request, food_routine:InsertFoodRoutine)->FoodRoutineSchema:
     with request.app.session_maker() as temp_session:
        session:Session = temp_session
        food_repo:FoodRoutineRepo = request.app.repositories.food_routine_repo(session)
        result = food_repo.add(food_routine)
        return result

def get_food_routine(request:Request, food_routine_id:int)->UpdateFoodRoutine:
    with request.app.session_maker() as temp_session:
        session:Session = temp_session
        food_repo:FoodRoutineRepo = request.app.repositories.food_routine_repo(session)
        return food_repo.get(food_routine_id)

def update_food_routine(request:Request, data:UpdateFoodRoutine)->FoodRoutineSchema:
    with request.app.session_maker() as temp_session:
        session:Session = temp_session
        food_repo:FoodRoutineRepo = request.app.repositories.food_routine_repo(session)
        result = food_repo.update(data)
        return result

def delete_food_routine(request:Request, id:int):
    with request.app.session_maker() as temp_session:
        session:Session = temp_session
        food_repo:FoodRoutineRepo = request.app.repositories.food_routine_repo(session)
        return food_repo.delete(id)