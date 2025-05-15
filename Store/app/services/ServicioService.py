from sqlalchemy.orm import Session
from app.models.Servicio import Servicio
from app.schemas.servicio import ServicioCreate, ServicioUpdate
from fastapi import HTTPException

def crear_servicio(db: Session, servicio: ServicioCreate):
    existente = db.query(Servicio).filter(Servicio.codigo_interno == servicio.codigo_interno).first()
    if existente:
        raise HTTPException(status_code=400, detail="Código de servicio ya existe")
    nuevo = Servicio(**servicio.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def obtener_servicios(db: Session):
    return db.query(Servicio).filter(Servicio.activo == True, Servicio.temporal == False).all()

def obtener_servicio_por_id(db: Session, servicio_id: int):
    return db.query(Servicio).filter(Servicio.id == servicio_id).first()

def actualizar_servicio(db: Session, servicio_id: int, data: ServicioUpdate):
    servicio = obtener_servicio_por_id(db, servicio_id)
    if servicio and not servicio.temporal:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(servicio, key, value)
        db.commit()
        db.refresh(servicio)
    return servicio

def inactivar_servicio(db: Session, servicio_id: int):
    servicio = obtener_servicio_por_id(db, servicio_id)
    if servicio:
        servicio.activo = False
        db.commit()
    return servicio
