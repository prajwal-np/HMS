from fastapi import Request
from schemas.tenant_schema import TenantSchema, InsertTenant, UpdateTenant
from sqlalchemy.orm import Session
from data_access.tenant.tenant_repository import TenantRepo

def insert_tenant(request:Request, tenant:InsertTenant)->TenantSchema:
     with request.app.session_maker() as temp_session:
        session:Session = temp_session
        tenant_repo:TenantRepo = request.app.repositories.tenant_repo(session)
        result = tenant_repo.add(tenant)
        return result

def get_tenant(request:Request, tenant_id:int)->UpdateTenant:
    with request.app.session_maker() as temp_session:
        session:Session = temp_session
        tenant_repo:TenantRepo = request.app.repositories.tenant_repo(session)
        return tenant_repo.get(tenant_id)

def update_tenant(request:Request, data:UpdateTenant)->TenantSchema:
    with request.app.session_maker() as temp_session:
        session:Session = temp_session
        tenant_repo:TenantRepo = request.app.repositories.tenant_repo(session)
        result = tenant_repo.update(data)
        return result

def delete_tenant(request:Request, id:int)->str:
    with request.app.session_maker() as temp_session:
        session:Session = temp_session
        tenant_repo:TenantRepo = request.app.repositories.tenant_repo(session)
        return tenant_repo.delete(id)