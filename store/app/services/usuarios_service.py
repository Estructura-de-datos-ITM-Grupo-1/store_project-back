# CONFIG DE USUARIOS
import json
from typing import List
from typing import Union
from fastapi import HTTPException
from app.core.auth import encriptar_password 
from app.schemas.usuarios_schema import CrearUsuario, ModificarUsuario
from app.utils.usuarios_helpers import obtener_usuario_por_username
from app.core.paths import USUARIOS_JSON as DATA_FILE


def _cargar_usuarios() -> List[dict]:
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def _guardar_usuarios(usuarios: List[dict]):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=2)


def crear_usuario(usuario: CrearUsuario):
    usuarios = _cargar_usuarios()
    if any(u["nombre_usuario"] == usuario.nombre_usuario for u in usuarios):
        raise HTTPException(status_code=400, detail="El nombre de usuario ya existe")
    
    nuevo = usuario.model_dump()
    nuevo["contrasena"] = encriptar_password(nuevo["contrasena"])  
    nuevo["activo"] = True
    usuarios.append(nuevo)
    _guardar_usuarios(usuarios)
    return {"mensaje": "Usuario creado exitosamente"}



def modificar_usuario(nombre_usuario: str, datos: ModificarUsuario):
    usuarios = _cargar_usuarios()
    for u in usuarios:
        if u["nombre_usuario"] == nombre_usuario:
            if datos.campo not in u:
                raise HTTPException(status_code=400, detail="Campo inválido")
            u[datos.campo] = datos.nuevo_valor
            _guardar_usuarios(usuarios)
            return {"mensaje": f"Usuario '{nombre_usuario}' modificado exitosamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


def inactivar_usuario(nombre_usuario: str):
    usuarios = _cargar_usuarios()
    for u in usuarios:
        if u["nombre_usuario"] == nombre_usuario:
            u["activo"] = False
            _guardar_usuarios(usuarios)
            return {"mensaje": f"Usuario '{nombre_usuario}' ha sido inactivado"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


def mostrar_usuarios(solo_activos: bool = True):
    usuarios = _cargar_usuarios()
    if solo_activos:
        usuarios = [u for u in usuarios if u.get("activo")]
    return usuarios
