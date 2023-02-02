from ..repositories_base import BaseRepository
from .food_routine_model import FoodRoutine
from typing import Union
from schemas.food_routine_schema import InsertFoodRoutine, FoodRoutineSchema, UpdateFoodRoutine

class FoodRoutineRepo(BaseRepository):

    def add(self, data: InsertFoodRoutine)->FoodRoutineSchema:
        try:
            food_routine = FoodRoutine(
                 building= data.building,
                 lunch_time= data.lunch_time,
                 break_fast_time= data.break_fast_time,
                 snack_time= data.snack_time,
                 dinner_time= data.dinner_time,
            )
            return super().add(food_routine)
        except Exception as e:
            print(e)
            raise e
    
    def get(self, id: Union[str, int]):
        return super().get(FoodRoutine,id)
    
    def update(self, data: UpdateFoodRoutine)->FoodRoutineSchema:
        food_routine:FoodRoutine = self.session.query(FoodRoutine).get(data.id)
        food_routine.update(data)
        result = super().add(food_routine)
        print(result)
        return result

    def delete(self, id: Union[str, int]):
        return super().delete(FoodRoutine, id)