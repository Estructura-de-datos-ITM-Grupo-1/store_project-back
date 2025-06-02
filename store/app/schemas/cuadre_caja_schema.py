from pydantic import BaseModel
from datetime import date
from typing import List
from pydantic import BaseModel, Field


class VentaDetalle(BaseModel):
    descripcion: str
    cantidad: int
    precio_unitario: float
    metodo_pago: str


class ResumenVentas(BaseModel):
    fecha: date
    ventas: List[VentaDetalle]
    
class VentaDetalle(BaseModel):
    descripcion: str = Field(..., min_length=1, max_length=255, title="Descripción del producto o servicio")
    cantidad: int = Field(..., gt=0, title="Cantidad vendida")
    precio_unitario: float = Field(..., gt=0, title="Precio unitario de la venta")
    metodo_pago: str = Field(..., min_length=3, max_length=50, title="Método de pago utilizado")


class EgresoDetalle(BaseModel):
    fecha: date
    motivo_egreso: str
    valor: float
    identificacion_receptor: str
    
class CuadreCajaBase(BaseModel):
    fecha: date
    usuario: str
    base_caja: float
    total_ingresos: float
    total_egresos: float
    comentario: str | None = None

class CuadreCajaCrear(CuadreCajaBase):
    efectivo_contado: float

class CuadreCajaCrear(CuadreCajaBase):
    efectivo_contado: float
    ventas: List[VentaDetalle]
    