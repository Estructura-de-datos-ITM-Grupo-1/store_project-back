from fastapi import APIRouter, HTTPException
from typing import List
from app.services import inventario_service
from app.schemas.inventario_schema import (
    ProductoIn,
    ProductoOut,
    MovimientoIn,
    MovimientoOut
)


router = APIRouter(tags=["Inventario"])

@router.post("/producto", response_model=ProductoOut)
def crear_producto(producto: ProductoIn):
    return inventario_service.registrar_producto(
        nombre=producto.nombre,
        categoria=producto.categoria,
        cantidad=producto.cantidad
    )

@router.get("/productos", response_model=List[ProductoOut])
def listar_productos():
    return inventario_service.listar_productos_activos()

@router.post("/movimiento", response_model=MovimientoOut)
def registrar_movimiento(mov: MovimientoIn):
    try:
        return inventario_service.registrar_movimiento(
            id_producto=mov.id_producto,
            tipo=mov.tipo,
            cantidad=mov.cantidad,
            usuario=mov.usuario
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/movimientos", response_model=List[MovimientoOut])
def listar_movimientos():
    return inventario_service.listar_movimientos()