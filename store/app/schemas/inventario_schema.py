from pydantic import BaseModel

class ProductoBase(BaseModel):
    nombre: str
    stock: int
    categoria: str
    precio: float
    activo: bool = True

class ProductoCreate(ProductoBase):
    id: int

class ProductoOut(ProductoBase):
    id: int

    class Config:
        orm_mode = True