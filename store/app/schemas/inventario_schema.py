from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime

# Entrada del producto al crear o modificar
class ProductoIn(BaseModel):
    codigo: str
    nombre: str
    descripcion: Optional[str] = None
    precio_unitario: float
    cantidad: int

# Salida del producto (lo que se devuelve al cliente)
class ProductoOut(ProductoIn):
    id: str

# Entrada de un movimiento (cuando se hace un registro)
class MovimientoIn(BaseModel):
    producto_id: str
    tipo: Literal["entrada", "salida"]
    cantidad: int
    usuario: str
    fecha_hora: datetime
    observaciones: Optional[str] = None

class MovimientoOut(MovimientoIn):
    id: str 