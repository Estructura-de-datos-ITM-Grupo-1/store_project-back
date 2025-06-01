from typing import List
from fastapi import APIRouter, Depends
from app.schemas.cuadre_caja_schema import CuadreCajaBase, ResumenVentas, EgresoDetalle, CuadreCajaCrear
from app.services.cuadre_caja_service import (
    calcular_utilidad, 
    organizar_ventas_por_metodo, 
    calcular_total_egresos,
    validar_cuadre,
    calcular_dinero_consignar
    )


router = APIRouter(prefix="/Cuadre_Caja", tags=["Cuadre Caja"])

@router.post("/cuadre/")
def registrar_cuadre(cuadre: CuadreCajaBase):
    utilidad = calcular_utilidad(cuadre.total_ingresos, cuadre.total_egresos)
    return {"mensaje": "Cuadre registrado", "utilidad": utilidad}

@router.post("/resumenventas/")
def generar_resumen_ventas(resumen: ResumenVentas):
    ventas_por_metodo = organizar_ventas_por_metodo(resumen.ventas)
    
    return {
        "fecha": resumen.fecha,
        "ventas_por_metodo": ventas_por_metodo
    }

@router.post("/registro_egresos/")
def registrar_egresos(egresos: List[EgresoDetalle]):
    total_egresos = calcular_total_egresos(egresos)
    return {
        "mensaje": "Egresos registrados",
        "total_egresos": total_egresos,
        "detalle": egresos
    }

@router.post("/conteo_efectivo/")
def registrar_conteo(cuadre: CuadreCajaCrear):
    resultado = validar_cuadre(cuadre.efectivo_contado, cuadre.total_ingresos, cuadre.total_egresos)
    return {"mensaje": "Conteo de efectivo registrado", "resultado": resultado}


@router.post("/dinero_consignar/")
def obtener_dinero_consignar(cuadre: CuadreCajaCrear):
    total_ventas_efectivo = sum(venta.cantidad * venta.precio_unitario  for venta in cuadre.ventas if venta.metodo_pago == "Efectivo")
    dinero_consignar = calcular_dinero_consignar(total_ventas_efectivo, cuadre.base_caja)
    
    return {"dinero_consignar": dinero_consignar}