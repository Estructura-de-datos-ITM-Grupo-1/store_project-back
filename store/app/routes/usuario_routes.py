from fastapi import APIRouter, Query
from app.schemas.usuarios_schema import CrearUsuario, ModificarUsuario
from app.services import usuarios_service

router = APIRouter(tags=["Usuarios"])

@router.post("/", summary="Crear un nuevo usuario")
def crear_usuario(usuario: CrearUsuario):
    return usuarios_service.crear_usuario(usuario)

@router.patch("/{nombre_usuario}", summary="Modificar un campo de un usuario")
def modificar_usuario(nombre_usuario: str, datos: ModificarUsuario):
    return usuarios_service.modificar_usuario(nombre_usuario, datos)

@router.patch("/{nombre_usuario}/inactivar", summary="Inactivar un usuario")
def inactivar_usuario(nombre_usuario: str):
    return usuarios_service.inactivar_usuario(nombre_usuario)

@router.get("/", summary="Listar usuarios")
def listar_usuarios(solo_activos: bool = Query(True, description="Mostrar solo usuarios activos")):
    return usuarios_service.mostrar_usuarios(solo_activos)
