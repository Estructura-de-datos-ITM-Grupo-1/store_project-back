from pydantic import BaseModel, Field, validator
from typing import Optional, List
from enum import Enum
from datetime import datetime

class MotivoMovimiento(str, Enum):
    VENTA = "venta"
    REPOSICION = "reposición"
    DANO = "daño"
    PERDIDA = "pérdida"
    DEVOLUCION = "devolución"

class ProductoBase(BaseModel):
    codigo_interno: str = Field(..., min_length=3, max_length=50)
    nombre: str = Field(..., max_length=100)
    descripcion: Optional[str] = Field(None, max_length=250)
    marca: str = Field(..., max_length=50)
    referencia: str = Field(..., max_length=50)
    colores: List[str] = Field(default_factory=list)
    categoria: str = Field(..., max_length=50)
    valor_costo: float = Field(..., gt=0)
    valor_venta: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)

    @validator("valor_venta")
    def validar_valor_venta(cls, v, values):
        if "valor_costo" in values and v <= values["valor_costo"]:
            raise ValueError("El valor de venta debe ser mayor al de costo")
        return v

class ProductoCreate(ProductoBase):
    pass

class ProductoOut(ProductoBase):
    id: int
    fecha_ingreso: datetime
    activo: bool

class ProductoUpdate(BaseModel):
    valor_costo: Optional[float] = Field(None, gt=0)
    valor_venta: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)