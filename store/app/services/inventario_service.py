import os
import json
from datetime import datetime
from typing import List, Optional
from app.core.paths import INVENTARIO_JSON, MOVIMIENTOS_JSON


def leer_inventario() -> List[dict]:
    if not os.path.exists(INVENTARIO_JSON):
        return []
    with open(INVENTARIO_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def escribir_inventario(data: List[dict]):
    with open(INVENTARIO_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def leer_movimientos() -> List[dict]:
    if not os.path.exists(MOVIMIENTOS_JSON):
        return []
    with open(MOVIMIENTOS_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def escribir_movimientos(data: List[dict]):
    with open(MOVIMIENTOS_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# Funcionalidades 

def crear_producto(nombre: str, codigo: str, cantidad: int, precio: float, categoria: str, usuario: str):
    inventario = leer_inventario()
    if any(prod['codigo'] == codigo for prod in inventario):
        raise ValueError("El producto ya existe")

    nuevo_producto = {
        "id": str(len(inventario) + 1),
        "nombre": nombre,
        "codigo": codigo,
        "cantidad": cantidad,
        "precio_unitario": precio,
        "categoria": categoria
    }
    inventario.append(nuevo_producto)
    escribir_inventario(inventario)
    registrar_movimiento("registro", codigo, cantidad, usuario)
    return nuevo_producto

def registrar_movimiento(tipo: str, codigo: str, cantidad: int, usuario: str):
    movimientos = leer_movimientos()
    movimientos.append({
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tipo": tipo,
        "codigo_producto": codigo,
        "cantidad": cantidad,
        "usuario": usuario
    })
    escribir_movimientos(movimientos)

def hacer_movimiento(tipo: str, codigo: str, cantidad: int, usuario: str):
    inventario = leer_inventario()
    producto = next((p for p in inventario if p['codigo'] == codigo), None)
    if not producto:
        raise ValueError("Producto no encontrado")

    if tipo == "salida" and producto['cantidad'] < cantidad:
        raise ValueError("Cantidad insuficiente en inventario")

    if tipo == "entrada":
        producto['cantidad'] += cantidad
    elif tipo == "salida":
        producto['cantidad'] -= cantidad

    escribir_inventario(inventario)
    registrar_movimiento(tipo, codigo, cantidad, usuario)
    return producto

def obtener_stock() -> List[dict]:
    return leer_inventario()

def buscar_producto(codigo: str) -> Optional[dict]:
    inventario = leer_inventario()
    return next((p for p in inventario if p['codigo'] == codigo), None)

def actualizar_producto(codigo: str, campo: str, nuevo_valor, usuario: str):
    inventario = leer_inventario()
    for prod in inventario:
        if prod['codigo'] == codigo:
            valor_anterior = prod.get(campo)
            prod[campo] = nuevo_valor
            escribir_inventario(inventario)
            registrar_movimiento("modificacion", codigo, 0, usuario)
            return prod
    raise ValueError("Producto no encontrado")

def listar_movimientos() -> List[dict]:
    return leer_movimientos()