from ..repositories_base import BaseRepository
from typing import Union
from schemas.tenant_schema import InsertTenant, TenantSchema, UpdateTenant

class TenantRepo(BaseRepository):
    def add(self, data: InsertTenant)->TenantSchema:
        return
    
    def get(self, id: Union[str, int]):
        return
    
    def update(self, data: UpdateTenant)->TenantSchema:
        return

    def delete(self, id: Union[str, int]):
        return