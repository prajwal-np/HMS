from fastapi import Request
from sqlalchemy.orm import Session
from data_access.building.building_repository import BuildingRepo, InsertBuilding, BuildingSchema, UpdateBuilding

def insert_building(request:Request, building: InsertBuilding)->BuildingSchema:
    with request.app.session_maker() as temp_session:
        session:Session = temp_session
        building_repo: BuildingRepo = request.app.repositories.building_repo(session)
        result = building_repo.add(building)
        return result

def get_building(request:Request, building_id)->UpdateBuilding:
    with request.app.session_maker() as temp_session:
        session:Session = temp_session
        building_repo: BuildingRepo = request.app.repositories.building_repo(session)
        result = building_repo.get(building_id)
        return result

def update_building(request:Request, building:UpdateBuilding):
    with request.app.session_maker() as temp_session:
        session:Session = temp_session
        building_repo: BuildingRepo = request.app.repositories.building_repo(session)
        result = building_repo.update(building)
        return result

def delete_building(request:Request, building_id:int)->str:
      with request.app.session_maker() as temp_session:
        session:Session = temp_session
        building_repo: BuildingRepo = request.app.repositories.building_repo(session)
        result = building_repo.delete(building_id)
        return result