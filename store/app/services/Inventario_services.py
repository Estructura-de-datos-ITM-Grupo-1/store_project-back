from datetime import datetime
from typing import Optional, List
from .Inventario_json import leer_json, escribir_json
from ..schemas.Inventario_schemas import ProductoOut, MotivoMovimiento

ARCHIVO_INVENTARIO = "Inventario_data.json"
ARCHIVO_MOVIMIENTOS = "Inventario_movimientos_data.json" 

class ProductoService:
    @staticmethod
    def _generar_id() -> int:
        productos = leer_json(ARCHIVO_INVENTARIO)
        return max([p["id"] for p in productos], default=0) + 1

    @staticmethod
    def crear_producto(producto_data: dict) -> ProductoOut:
        productos = leer_json(ARCHIVO_INVENTARIO)
        
        if any(p["codigo_interno"] == producto_data["codigo_interno"] for p in productos):
            raise ValueError("El código interno ya existe")

        nuevo_producto = {
            "id": ProductoService._generar_id(),
            **producto_data,
            "fecha_ingreso": datetime.now().isoformat(),
            "activo": producto_data["stock"] > 0
        }
        
        productos.append(nuevo_producto)
        escribir_json(ARCHIVO_INVENTARIO, productos)
        return ProductoOut(**nuevo_producto)

    @staticmethod
    def buscar_por_codigo(codigo: str) -> Optional[ProductoOut]:
        productos = leer_json(ARCHIVO_INVENTARIO)
        producto = next((p for p in productos if p["codigo_interno"] == codigo), None)
        return ProductoOut(**producto) if producto else None

    @staticmethod
    def obtener_todos() -> List[ProductoOut]:
        return [ProductoOut(**p) for p in leer_json(ARCHIVO_INVENTARIO)]

    @staticmethod
    def actualizar_stock(producto_id: int, cantidad: int, motivo: MotivoMovimiento, usuario: str) -> ProductoOut:
        productos = leer_json(ARCHIVO_INVENTARIO)
        movimientos = leer_json(ARCHIVO_MOVIMIENTOS)

        producto = next((p for p in productos if p["id"] == producto_id), None)
        if not producto:
            raise ValueError("Producto no encontrado")

        movimiento = {
            "producto_id": producto_id,
            "cantidad_anterior": producto["stock"],
            "cantidad_nueva": producto["stock"] + cantidad,
            "motivo": motivo.value,
            "usuario": usuario,
            "fecha": datetime.now().isoformat()
        }
        movimientos.append(movimiento)
        escribir_json(ARCHIVO_MOVIMIENTOS, movimientos)

        producto["stock"] += cantidad
        producto["activo"] = producto["stock"] > 0
        escribir_json(ARCHIVO_INVENTARIO, productos)
        
        return ProductoOut(**producto)