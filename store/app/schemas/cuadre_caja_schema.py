from pydantic import BaseModel
from datetime import date
from typing import List
from typing import Optional


class VentaDetalle(BaseModel):
    descripcion: str
    cantidad: int
    precio_unitario: float
    metodo_pago: str


class ResumenVentas(BaseModel):
    fecha: date
    ventas: List[VentaDetalle]

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
    comentario: Optional[str] = None

class CuadreCajaCrear(CuadreCajaBase):
    efectivo_contado: float

class CuadreCajaCrear(CuadreCajaBase):
    efectivo_contado: float
    ventas: List[VentaDetalle]
    