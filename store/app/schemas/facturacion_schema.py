from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ItemFactura(BaseModel):
    descripcion: str
    cantidad: int
    precio_unitario: float
    metodo_pago: str

class FacturaCrear(BaseModel):
    cliente_id: str
    items: List[ItemFactura]
    total: float
    observaciones: Optional[str] = None
    usuario: str

class FacturaRespuesta(FacturaCrear):
    id: str
    fecha: datetime