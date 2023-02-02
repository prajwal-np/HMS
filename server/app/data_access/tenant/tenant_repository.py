from ..repositories_base import BaseRepository
from .tenant_model import Tenant
from typing import Union
from schemas.tenant_schema import UpdateTenant,TenantSchema, InsertTenant

class TenantRepo(BaseRepository):

    def add(self, data: InsertTenant)->TenantSchema:
        try:
            tenant = Tenant(
                 building= data.building,
                 room_type= data.room_type,
                 current_status= data.current_status,
                 user= data.user,
            )
            return super().add(tenant)
        except Exception as e:
            print(e)
            raise e
    
    def get(self, id: Union[str, int]):
        return super().get(Tenant,id)
    
    def update(self, data: UpdateTenant)->TenantSchema:
        tenant:Tenant = self.session.query(Tenant).get(data.id)
        tenant.update(data)
        result = super().add(tenant)
        print(result)
        return result

    def delete(self, id: Union[str, int]):
        return super().delete(Tenant, id)