from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.facturacion_schema import FacturaCrear, FacturaRespuesta
from app.services import facturacion_service

router = APIRouter(tags=["Facturacion"])

@router.post("/factura", response_model=FacturaRespuesta)
def crear_factura(factura: FacturaCrear):
    try:
        return facturacion_service.crear_factura(factura)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/facturas", response_model=List[FacturaRespuesta])
def listar_facturas():
    return facturacion_service.obtener_facturas()