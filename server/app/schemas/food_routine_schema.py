class FoodRoutineSchema:
    building: int
    lunch_time: int
    break_fast_time: int
    snack_time: int
    dinner_time: int

class InsertFoodRoutine(FoodRoutineSchema):
    pass

class UpdateFoodRoutine(InsertFoodRoutine):
    id: int