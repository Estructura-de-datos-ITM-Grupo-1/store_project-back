from pydantic import BaseModel, EmailStr

class ClienteCrear(BaseModel):
    nombre: str
    tipo_id: str
    numero_id: str
    telefono: str
    email: EmailStr
    direccion: str

class ClienteModificar(BaseModel):
    campo: str
    nuevo_valor: str

class ClienteOut(BaseModel):
    id: str
    nombre: str
    tipo_id: str
    numero_id: str
    telefono: str
    email: EmailStr
    direccion: str
    estado: str