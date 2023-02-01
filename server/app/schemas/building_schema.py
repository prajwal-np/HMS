from pydantic import BaseModel

class BuildingSchema(BaseModel):
    createdBy: int
    name: str
    location: str
    capacity: int
    single_bed: int
    double_bed: int
    three_bed: int
    four_bed: int

class InsertBuilding(BuildingSchema):
    pass

class UpdateBuilding(BuildingSchema):
    id: int
    