from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime


class ProductoBase(BaseModel):
    codigo: str
    nombre: str
    descripcion: Optional[str] = None
    precio_unitario: float
    cantidad: int


class ProductoCrear(ProductoBase):
    pass


class ProductoRespuesta(ProductoBase):
    id: str


class MovimientoInventario(BaseModel):
    producto_id: str
    tipo: Literal["entrada", "salida"]
    cantidad: int
    usuario: str
    fecha_hora: datetime
    observaciones: Optional[str] = None
