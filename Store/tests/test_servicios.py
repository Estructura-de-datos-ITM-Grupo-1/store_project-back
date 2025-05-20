import sys
import os
from fastapi.testclient import TestClient

# Asegurar que el path incluya Store/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from server import app

client = TestClient(app)

# -----------------------
# ✅ TESTS UNITARIOS (JSON)
# -----------------------

def test_crear_servicio():
    response = client.post("/api/v1/servicios/", json={
        "codigo_interno": "TEST001",
        "descripcion": "Servicio de prueba",
        "valor_total": 50000,
        "temporal": False,
        "creado_por": "tester"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["codigo_interno"] == "TEST001"

def test_listar_servicios():
    response = client.get("/api/v1/servicios/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_obtener_servicio_por_id():
    response_crear = client.post("/api/v1/servicios/", json={
        "codigo_interno": "TEST002",
        "descripcion": "Servicio de prueba ID",
        "valor_total": 100000,
        "temporal": False,
        "creado_por": "tester"
    })
    assert response_crear.status_code == 200
    servicio_id = response_crear.json()["id"]

    response_get = client.get(f"/api/v1/servicios/{servicio_id}")
    assert response_get.status_code == 200
    assert response_get.json()["codigo_interno"] == "TEST002"

def test_actualizar_servicio():
    response_crear = client.post("/api/v1/servicios/", json={
        "codigo_interno": "TEST003",
        "descripcion": "Servicio viejo",
        "valor_total": 50000,
        "temporal": False,
        "creado_por": "tester"
    })
    assert response_crear.status_code == 200
    servicio_id = response_crear.json()["id"]

    response_update = client.put(f"/api/v1/servicios/{servicio_id}", json={
        "descripcion": "Servicio actualizado",
        "valor_total": 99999
    })
    assert response_update.status_code == 200
    assert response_update.json()["descripcion"] == "Servicio actualizado"
    assert response_update.json()["valor_total"] == 99999

def test_inactivar_servicio():
    response_crear = client.post("/api/v1/servicios/", json={
        "codigo_interno": "TEST004",
        "descripcion": "Servicio a inactivar",
        "valor_total": 20000,
        "temporal": False,
        "creado_por": "tester"
    })
    assert response_crear.status_code == 200
    servicio_id = response_crear.json()["id"]

    response_inactivar = client.patch(f"/api/v1/servicios/{servicio_id}/inactivar")
    assert response_inactivar.status_code == 200
    assert response_inactivar.json()["activo"] == False
