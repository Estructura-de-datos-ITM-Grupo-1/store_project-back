from pydantic import BaseModel
from typing import Optional, Literal

class CrearUsuario(BaseModel):
    nombre_completo : str
    nombre_usuario : str
    contrasena : str
    correo : Optional[str] = None
    rol : Literal["administrador", "comercial", "vendedor"]
    
class ModificarUsuario(BaseModel):
    campo: str
    nuevo_valor: str
    
