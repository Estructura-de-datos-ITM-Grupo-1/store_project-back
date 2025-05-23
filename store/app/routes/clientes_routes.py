from fastapi import APIRouter, Depends, HTTPException
from typing import List

from app.schemas.cliente_schema import ClienteCrear, ClienteModificar, ClienteOut
from app.services.clientes_service import (
    registrar_cliente,
    modificar_cliente,
    inactivar_cliente,
    listar_clientes_activos
)
def get_current_user(): #VERSION PARA PRUEBAS, UNA VEZ SE TENGA EL AUTH REAL HAY QUE CAMBIAR ESTO
    return {"rol": "administrador"}

router = APIRouter(prefix="/clientes", tags=["Clientes"])

# Crear cliente
@router.post("/", response_model=ClienteOut)
def crear_cliente(cliente: ClienteCrear, usuario=Depends(get_current_user)):
    try:
        return registrar_cliente(
            rol=usuario["rol"],
            nombre=cliente.nombre,
            tipo_id=cliente.tipo_id,
            numero_id=cliente.numero_id,
            telefono=cliente.telefono,
            email=cliente.email,
            direccion=cliente.direccion
        )
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))


# Modificar cliente
@router.put("/{cliente_id}", response_model=ClienteOut)
def actualizar_cliente(cliente_id: str, datos: ClienteModificar, usuario=Depends(get_current_user)):
    try:
        return modificar_cliente(
            rol=usuario["rol"],
            cliente_id=cliente_id,
            campo=datos.campo,
            nuevo_valor=datos.nuevo_valor
        )
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# Inactivar cliente
@router.delete("/{cliente_id}")
def eliminar_cliente(cliente_id: str, usuario=Depends(get_current_user)):
    try:
        inactivar_cliente(rol=usuario["rol"], cliente_id=cliente_id)
        return {"mensaje": f"Cliente {cliente_id} inactivado exitosamente."}
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# Listar clientes activos
@router.get("/", response_model=List[ClienteOut])
def obtener_clientes_activos():
    return listar_clientes_activos()