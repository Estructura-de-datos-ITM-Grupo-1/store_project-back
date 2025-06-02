import json
import os
from datetime import datetime
from typing import List, Optional
from fastapi import HTTPException
from app.schemas.servicio import ServicioCreate, ServicioUpdate, ServicioOut
from app.core.paths import SERVICIOS_JSON as DATA_FILE


def _cargar_servicios() -> List[dict]:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _guardar_servicios(servicios: List[dict]):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(servicios, f, indent=2, default=str)


def crear_servicio(servicio: ServicioCreate) -> ServicioOut:
    servicios = _cargar_servicios()
    if any(s["codigo_interno"] == servicio.codigo_interno for s in servicios):
        raise HTTPException(status_code=400, detail="Código de servicio ya existe")
    nuevo_id = max([s["id"] for s in servicios], default=0) + 1
    nuevo = {
        "id": nuevo_id,
        "codigo_interno": servicio.codigo_interno,
        "descripcion": servicio.descripcion,
        "valor_total": servicio.valor_total,
        "temporal": servicio.temporal,
        "creado_por": servicio.creado_por,
        "fecha_creacion": datetime.utcnow().isoformat(),
        "activo": True
    }
    servicios.append(nuevo)
    _guardar_servicios(servicios)
    return ServicioOut(**nuevo)


def obtener_servicios() -> List[ServicioOut]:
    servicios = _cargar_servicios()
    activos = [s for s in servicios if s.get("activo") and not s.get("temporal")]
    return [ServicioOut(**s) for s in activos]


def obtener_servicio_por_id(servicio_id: int) -> Optional[ServicioOut]:
    servicios = _cargar_servicios()
    for s in servicios:
        if s["id"] == servicio_id:
            return ServicioOut(**s)
    return None


def actualizar_servicio(servicio_id: int, data: ServicioUpdate) -> ServicioOut:
    servicios = _cargar_servicios()
    for idx, s in enumerate(servicios):
        if s["id"] == servicio_id:
            if s.get("temporal"):
                raise HTTPException(status_code=400, detail="No se puede modificar un servicio temporal")
            actualizado = {**s, **data.model_dump(exclude_unset=True)}
            servicios[idx] = actualizado
            _guardar_servicios(servicios)
            return ServicioOut(**actualizado)
    raise HTTPException(status_code=404, detail="Servicio no encontrado")


def inactivar_servicio(servicio_id: int) -> ServicioOut:
    servicios = _cargar_servicios()
    for idx, s in enumerate(servicios):
        if s["id"] == servicio_id:
            s["activo"] = False
            servicios[idx] = s
            _guardar_servicios(servicios)
            return ServicioOut(**s)
    raise HTTPException(status_code=404, detail="Servicio no encontrado")
