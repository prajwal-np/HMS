from sqlalchemy.orm import Session
from typing import Union

class BaseRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def add(self,data):
        print(data)
        pass
    
    def get(self,id: Union[str, int]):
        pass
    
    def update(self,id: Union[str, int]):
        pass

    def delete(self,id: Union[str, int]):
        pass