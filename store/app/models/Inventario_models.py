from datetime import datetime
from typing import List

class Producto:
    def __init__(self, id: int, codigo_interno: str, nombre: str, marca: str, referencia: str, colores: List[str],
                 stock: int, valor_costo: float, valor_venta: float, categoria: str, descripcion: str = "", fecha_ingreso: str = None,
                 activo: bool = None):
        
        self.id = id
        self.codigo_interno = codigo_interno
        self.nombre = nombre
        self.marca = marca
        self.referencia = referencia
        self.colores = colores
        self.stock = stock
        self.valor_costo = valor_costo
        self.valor_venta = valor_venta
        self.categoria = categoria
        self.descripcion = descripcion
        self.fecha_ingreso = fecha_ingreso or datetime.now().isoformat()
        self.activo = stock > 0 if activo is None else activo

    def to_dict(self):
        return self.__dict__