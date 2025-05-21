from collections import defaultdict
from typing import List
from app.schemas.cuadre_caja_schema import VentaDetalle, EgresoDetalle


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

def validar_cuadre(efectivo_contado: float, total_ingresos: float, total_egresos: float) -> dict:
    saldo_esperado = total_ingresos - total_egresos
    diferencia = efectivo_contado - saldo_esperado
    estado = "Correcto" if diferencia == 0 else "Descuadre"    
    return {"Total de Ingresos": total_ingresos,"Total de Egresos": total_egresos, "efectivo_contado": efectivo_contado,"Utilidad del día": saldo_esperado, "diferencia": diferencia, "estado": estado}

def calcular_dinero_consignar(total_ventas_efectivo: float, base_caja: float) -> float:
    """Calcula el dinero que se debe consignar: efectivo recibido menos la base inicial de caja"""
    return total_ventas_efectivo - base_caja