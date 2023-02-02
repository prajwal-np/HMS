from schemas.tenant_schema import TenantSchema, InsertTenant, UpdateTenant
from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from starlette.requests import Request
from utils.middleware import Middleware
from services.tenant_service import delete_tenant,get_tenant,insert_tenant,update_tenant
router = APIRouter(prefix='/tenant',tags=['Tenant'], dependencies=[Depends(Middleware)])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TenantSchema)
def create_tenant(request: Request, user: InsertTenant):
    try:
        result = insert_tenant(request, user)
        return result
    except Exception as error:
        print(error)
        raise HTTPException(status_code=403,detail='Cannot register')

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=TenantSchema)
def get_tenant_api(request: Request, id: int):
    try:
        result = get_tenant(request, id)
        return result
    except Exception as error:
        print(error)

@router.put("/", status_code=status.HTTP_200_OK, response_model=TenantSchema)
def update_tenant_api(request: Request, tenant: UpdateTenant):
    try:
        result = update_tenant(request, tenant)
        return result
    except Exception as error:
        print(error)

@router.delete("/{id}", status_code=status.HTTP_200_OK, response_model=str)
def delete_tenant_api(request: Request, id: str):
    try:
        result = delete_tenant(request, id)
        return result
    except Exception as error:
        print(error)
