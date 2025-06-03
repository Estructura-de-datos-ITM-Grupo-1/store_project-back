from fastapi import APIRouter, Query, Depends, HTTPException
from app.schemas.usuarios_schema import CrearUsuario, ModificarUsuario, LoginRequest
from app.services import usuarios_service
from app.core.auth import verificar_credenciales, crear_token_acceso, obtener_usuario_actual

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

@router.post("/login", summary="Iniciar sesión y obtener token JWT")
def login(datos: LoginRequest):
    usuario = verificar_credenciales(datos.nombre_usuario, datos.contrasena)
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return {"access_token": crear_token_acceso(usuario["nombre_usuario"])}
