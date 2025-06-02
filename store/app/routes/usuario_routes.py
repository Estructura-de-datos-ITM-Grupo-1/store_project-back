from fastapi import APIRouter, HTTPException
from app.schemas.servicio import ServicioCreate, ServicioUpdate, ServicioOut
from app.services import usuarios_service


router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/crearusuario")
def crearusuario():
    return usuarios_service.Administracion_usuarios.crear_usuario()

@router.post("/modificarusuario")
def modificar_usuario():
    return usuarios_service.Administracion_usuarios.modificar_usuario()
    
@router.post("/inactivarusuario")
def inactivar_usuario():
    return usuarios_service.Administracion_usuarios.inactivar_usuario()
        
@router.post("/mostrarusuarios")
def mostrar_usuarios():
    return usuarios_service.Administracion_usuarios.modificar_usuario()