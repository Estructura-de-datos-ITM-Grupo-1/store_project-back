import pytest
import json
from fastapi.testclient import TestClient
from server import app
from app.core.paths import USUARIOS_JSON

client = TestClient(app)

# -------------------------------
# Limpiar usuarios.json al inicio
# -------------------------------
def reset_usuarios():
    with open(USUARIOS_JSON, "w", encoding="utf-8") as f:
        json.dump([], f)

reset_usuarios()

# -------------------------------
# Datos de prueba
# -------------------------------
usuario_valido = {
    "nombre_usuario": "test_user",
    "nombre_completo": "Usuario Prueba",
    "contrasena": "clave123",
    "correo": "test@example.com",
    "rol": "vendedor"
}

modificacion_valida = {
    "campo": "nombre_completo",
    "nuevo_valor": "Usuario Actualizado"
}

login_valido = {
    "nombre_usuario": "test_user",
    "contrasena": "clave123"
}

# -------------------------------
# Crear usuario antes de todos los tests
# -------------------------------
def setup_module(module):
    client.post("/api/v1/usuarios/", json=usuario_valido)

# -------------------------------
# TEST: Crear usuario
# -------------------------------
def test_crear_usuario():
    # Ya se creó en setup_module, probamos duplicado
    response = client.post("/api/v1/usuarios/", json=usuario_valido)
    assert response.status_code == 400
    assert response.json()["detail"] == "El nombre de usuario ya existe"

# -------------------------------
# TEST: Login exitoso
# -------------------------------
def test_login_usuario():
    response = client.post("/api/v1/usuarios/login", json=login_valido)
    assert response.status_code == 200
    assert "access_token" in response.json()

# -------------------------------
# TEST: Modificar nombre completo
# -------------------------------
def test_modificar_usuario():
    response = client.patch("/api/v1/usuarios/test_user", json=modificacion_valida)
    assert response.status_code == 200
    assert response.json()["mensaje"].startswith("Usuario")

# -------------------------------
# TEST: Inactivar usuario
# -------------------------------
def test_inactivar_usuario():
    response = client.patch("/api/v1/usuarios/test_user/inactivar")
    assert response.status_code == 200
    assert "inactivado" in response.json()["mensaje"].lower()

# -------------------------------
# TEST: Listar usuarios inactivos también
# -------------------------------
def test_listar_usuarios_todos():
    response = client.get("/api/v1/usuarios/?solo_activos=false")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
