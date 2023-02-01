class TenantSchema:
    building:int
    room_type: str
    current_status: str
    user:int

class InsertTenant(TenantSchema):
    pass

class UpdateTenant(InsertTenant):
    id: int