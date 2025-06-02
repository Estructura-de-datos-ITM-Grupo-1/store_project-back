from typing import List
from fastapi import APIRouter
from app.schemas.cuadre_caja_schema import CuadreCajaBase, ResumenVentas, EgresoDetalle, CuadreCajaCrear
from app.services import cuadre_caja_service

router = APIRouter(tags=["Cuadre Caja"])

@router.post("/cuadre/")
def registrar_cuadre(cuadre: CuadreCajaBase):
    utilidad = cuadre_caja_service.calcular_utilidad(cuadre.total_ingresos, cuadre.total_egresos)
    return {"mensaje": "Cuadre registrado", "utilidad": utilidad}

@router.post("/resumenventas/")
def generar_resumen_ventas(resumen: ResumenVentas):
    ventas_por_metodo = cuadre_caja_service.organizar_ventas_por_metodo(resumen.ventas)
    return {"fecha": resumen.fecha, "ventas_por_metodo": ventas_por_metodo}

@router.post("/registro_egresos/")
def registrar_egresos(egresos: List[EgresoDetalle]):
    total_egresos = cuadre_caja_service.calcular_total_egresos(egresos)
    return {
        "mensaje": "Egresos registrados",
        "total_egresos": total_egresos,
        "detalle": egresos
    }

@router.post("/conteo_efectivo/")
def registrar_conteo(cuadre: CuadreCajaCrear):
    resultado = cuadre_caja_service.validar_cuadre(cuadre.efectivo_contado, cuadre.total_ingresos, cuadre.total_egresos)
    return {"mensaje": "Conteo de efectivo registrado", "resultado": resultado}

@router.post("/dinero_consignar/")
def obtener_dinero_consignar(cuadre: CuadreCajaCrear):
    total_ventas_efectivo = sum(
        venta.cantidad * venta.precio_unitario
        for venta in cuadre.ventas if venta.metodo_pago.lower() == "efectivo"
    )
    dinero_consignar = cuadre_caja_service.calcular_dinero_consignar(cuadre.ventas, cuadre.base_caja)
    return {"dinero_consignar": dinero_consignar}

@router.post("/guardar_cuadre/", summary="Guardar cuadre completo en JSON")
def guardar_cuadre(cuadre: CuadreCajaCrear):
    return cuadre_caja_service.guardar_cuadre(cuadre)

@router.get("/listar_cuadres/", summary="Listar todos los cuadres registrados")
def listar_cuadres():
    return cuadre_caja_service.listar_cuadres()
