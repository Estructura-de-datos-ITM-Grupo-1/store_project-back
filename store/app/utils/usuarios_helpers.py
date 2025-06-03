import json
from app.core.paths import USUARIOS_JSON as DATA_FILE

def obtener_usuario_por_username(nombre_usuario: str):
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            usuarios = json.load(f)
    except FileNotFoundError:
        return None

    for usuario in usuarios:
        if usuario["nombre_usuario"] == nombre_usuario:
            return usuario
    return None
