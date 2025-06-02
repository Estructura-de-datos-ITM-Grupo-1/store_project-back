from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class RegistroAuditoria(BaseModel):
    cliente_id: int
    accion: str  # 'crear', 'modificar', 'inactivar'
    usuario: str
    fecha: datetime
    detalles: Optional[str] = None
