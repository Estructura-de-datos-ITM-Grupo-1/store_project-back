from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class CrearUsuario(BaseModel):
    nombre_completo : str
    nombre_usuario : str
    contrasena : str
    correo : Optional[str] = None
    rol : str
    
class ModificarUsuario(BaseModel):
    campo: str
    nuevo_valor: str
    
