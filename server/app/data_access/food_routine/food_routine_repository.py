from ..repositories_base import BaseRepository
from typing import Union
from schemas.food_routine_schema import InsertFoodRoutine, FoodRoutineSchema, UpdateFoodRoutine

class FoodRoutineRepo(BaseRepository):
    def add(self, data: InsertFoodRoutine)->FoodRoutineSchema:
        return
    
    def get(self, id: Union[str, int]):
        return
    
    def update(self, data: UpdateFoodRoutine)->FoodRoutineSchema:
        return

    def delete(self, id: Union[str, int]):
        return