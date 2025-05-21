from fastapi import APIRouter, HTTPException
from app.schemas.servicio import ServicioCreate, ServicioUpdate, ServicioOut
from app.services import ServicioService

router = APIRouter(tags=["Servicios"])

@router.post("/", response_model=ServicioOut)
def crear(servicio: ServicioCreate):
    return ServicioService.crear_servicio(servicio)

@router.get("/", response_model=list[ServicioOut])
def listar():
    return ServicioService.obtener_servicios()

@router.get("/{servicio_id}", response_model=ServicioOut)
def obtener(servicio_id: int):
    servicio = ServicioService.obtener_servicio_por_id(servicio_id)
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return servicio

@router.put("/{servicio_id}", response_model=ServicioOut)
def actualizar(servicio_id: int, datos: ServicioUpdate):
    return ServicioService.actualizar_servicio(servicio_id, datos)

@router.patch("/{servicio_id}/inactivar", response_model=ServicioOut)
def inactivar(servicio_id: int):
    return ServicioService.inactivar_servicio(servicio_id)
