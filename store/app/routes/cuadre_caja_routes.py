from typing import List
from fastapi import APIRouter, Depends, Query
from app.schemas.cuadre_caja_schema import CuadreCajaBase, ResumenVentas, EgresoDetalle, CuadreCajaCrear, VentaDetalle
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

@router.get("/organizar-ventas/")
def generar_resumen_ventas(
    metodos_pago: List[str] = Query([]),
    descripciones: List[str] = Query([]),
    cantidades: List[int] = Query([]),
    precios_unitarios: List[float] = Query([])
):
    ventas = [
        VentaDetalle(
            descripcion=descripciones[i],
            cantidad=cantidades[i],
            precio_unitario=precios_unitarios[i],
            metodo_pago=metodos_pago[i]
        ) for i in range(len(metodos_pago))
    ]

    resumen = organizar_ventas_por_metodo(ventas)

    return {"ventas_por_metodo": resumen}


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