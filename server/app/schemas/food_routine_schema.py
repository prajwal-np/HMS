from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class FoodRoutineSchema(BaseModel):
    id:Optional[int]
    building: int
    lunch_time: datetime
    break_fast_time: datetime
    snack_time: datetime
    dinner_time: datetime

class InsertFoodRoutine(FoodRoutineSchema):
    pass

class UpdateFoodRoutine(InsertFoodRoutine):
    id: int