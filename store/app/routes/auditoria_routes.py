from fastapi import APIRouter
from app.services import auditoria_service

router = APIRouter(tags=["Auditoría"])

@router.get("/auditoria/clientes", summary="Listar eventos de auditoría de clientes")
def obtener_auditoria_clientes():
    return auditoria_service.listar_auditoria()
