from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.servicio import ServicioCreate, ServicioUpdate, ServicioOut
from app.services import ServicioService
from app.core.deps import get_db

router = APIRouter(tags=["Servicios"])

@router.post("/", response_model=ServicioOut)
def crear(servicio: ServicioCreate, db: Session = Depends(get_db)):
    return ServicioService.crear_servicio(db, servicio)

@router.get("/", response_model=list[ServicioOut])
def listar(db: Session = Depends(get_db)):
    return ServicioService.obtener_servicios(db)

@router.get("/{servicio_id}", response_model=ServicioOut)
def obtener(servicio_id: int, db: Session = Depends(get_db)):
    servicio = ServicioService.obtener_servicio_por_id(db, servicio_id)
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return servicio

@router.put("/{servicio_id}", response_model=ServicioOut)
def actualizar(servicio_id: int, datos: ServicioUpdate, db: Session = Depends(get_db)):
    return ServicioService.actualizar_servicio(db, servicio_id, datos)

@router.patch("/{servicio_id}/inactivar", response_model=ServicioOut)
def inactivar(servicio_id: int, db: Session = Depends(get_db)):
    return ServicioService.inactivar_servicio(db, servicio_id)
