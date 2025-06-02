import json
from typing import List
from fastapi import HTTPException
from collections import defaultdict
from app.schemas.cuadre_caja_schema import (
    CuadreCajaCrear,
    EgresoDetalle,
    VentaDetalle
)
from app.core.paths import CUADRE_CAJA_JSON as DATA_FILE


def _cargar_cuadres() -> List[dict]:
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def _guardar_cuadres(data: List[dict]):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, default=str)


def calcular_utilidad(ingresos: float, egresos: float) -> float:
    return ingresos - egresos


def organizar_ventas_por_metodo(ventas: List[VentaDetalle]) -> dict:
    resumen = defaultdict(list)
    for venta in ventas:
        resumen[venta.metodo_pago].append({
            "descripcion": venta.descripcion,
            "cantidad": venta.cantidad,
            "precio_unitario": venta.precio_unitario,
            "total": venta.cantidad * venta.precio_unitario
        })
    return resumen


def calcular_total_egresos(egresos: List[EgresoDetalle]) -> float:
    return sum(egreso.valor for egreso in egresos)


def calcular_total_ingresos(ventas: List[VentaDetalle]) -> float:
    return sum(v.cantidad * v.precio_unitario for v in ventas)


def calcular_dinero_consignar(ventas: List[VentaDetalle], base_caja: float) -> float:
    efectivo_total = sum(v.cantidad * v.precio_unitario for v in ventas if v.metodo_pago.lower() == "efectivo")
    return efectivo_total - base_caja


def validar_cuadre(efectivo_contado: float, total_ingresos: float, total_egresos: float) -> dict:
    saldo_esperado = total_ingresos - total_egresos
    diferencia = efectivo_contado - saldo_esperado
    estado = "Correcto" if diferencia == 0 else "Descuadre"
    return {"utilidad": saldo_esperado, "diferencia": diferencia, "estado": estado}


def guardar_cuadre(cuadre: CuadreCajaCrear):
    data = _cargar_cuadres()

    total_ingresos = calcular_total_ingresos(cuadre.ventas)
    total_egresos = calcular_total_egresos(cuadre.egresos)
    resultado = validar_cuadre(cuadre.efectivo_contado, total_ingresos, total_egresos)
    dinero_consignar = calcular_dinero_consignar(cuadre.ventas, cuadre.base_caja)

    registro = {
        "fecha": cuadre.fecha.isoformat(),
        "usuario": cuadre.usuario,
        "base_caja": cuadre.base_caja,
        "total_ingresos": total_ingresos,
        "total_egresos": total_egresos,
        "comentario": cuadre.comentario,
        "efectivo_contado": cuadre.efectivo_contado,
        "ventas": [v.model_dump() for v in cuadre.ventas],
        "egresos": [e.model_dump() for e in cuadre.egresos],
        "utilidad": resultado["utilidad"],
        "diferencia": resultado["diferencia"],
        "estado": resultado["estado"],
        "dinero_consignar": dinero_consignar
    }

    data.append(registro)
    _guardar_cuadres(data)
    return {"mensaje": "Cuadre guardado exitosamente", "cuadre": registro}


def listar_cuadres():
    return _cargar_cuadres()
