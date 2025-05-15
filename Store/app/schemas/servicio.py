from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ServicioBase(BaseModel):
    descripcion: str
    valor_total: float
    temporal: Optional[bool] = False

class ServicioCreate(ServicioBase):
    codigo_interno: str
    creado_por: Optional[str] = None

class ServicioUpdate(BaseModel):
    descripcion: Optional[str] = None
    valor_total: Optional[float] = None

class ServicioOut(ServicioBase):
    id: int
    codigo_interno: str
    creado_por: Optional[str]
    fecha_creacion: datetime
    activo: bool

    class Config:
        orm_mode = True
