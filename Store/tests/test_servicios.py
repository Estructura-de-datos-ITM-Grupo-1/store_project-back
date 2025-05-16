import sys
import os

# Asegurarse de que Store/ esté en el path para importar desde allí
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from server import app
from app.core.database import Base
from app.core.deps import get_db
from app.models.Servicio import Servicio
from config import DATABASE_URL

# Crear engine para MySQL
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear las tablas necesarias si no existen
Base.metadata.create_all(bind=engine)

# Función para limpiar la tabla antes de cada test
def limpiar_tabla_servicios():
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM servicios"))
        connection.commit()

# Sobrescribir la dependencia de get_db
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

# -----------------------
# ✅ TESTS UNITARIOS
# -----------------------

def test_crear_servicio():
    limpiar_tabla_servicios()

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
    # Crear uno nuevo
    response_crear = client.post("/api/v1/servicios/", json={
        "codigo_interno": "TEST002",
        "descripcion": "Servicio de prueba ID",
        "valor_total": 100000,
        "temporal": False,
        "creado_por": "tester"
    })
    assert response_crear.status_code == 200
    servicio_id = response_crear.json()["id"]

    # Obtenerlo por ID
    response_get = client.get(f"/api/v1/servicios/{servicio_id}")
    assert response_get.status_code == 200
    assert response_get.json()["codigo_interno"] == "TEST002"

def test_actualizar_servicio():
    # Crear uno nuevo
    response_crear = client.post("/api/v1/servicios/", json={
        "codigo_interno": "TEST003",
        "descripcion": "Servicio viejo",
        "valor_total": 50000,
        "temporal": False,
        "creado_por": "tester"
    })
    assert response_crear.status_code == 200
    servicio_id = response_crear.json()["id"]

    # Actualizar
    response_update = client.put(f"/api/v1/servicios/{servicio_id}", json={
        "descripcion": "Servicio actualizado",
        "valor_total": 99999
    })
    assert response_update.status_code == 200
    assert response_update.json()["descripcion"] == "Servicio actualizado"
    assert response_update.json()["valor_total"] == 99999

def test_inactivar_servicio():
    # Crear uno nuevo
    response_crear = client.post("/api/v1/servicios/", json={
        "codigo_interno": "TEST004",
        "descripcion": "Servicio a inactivar",
        "valor_total": 20000,
        "temporal": False,
        "creado_por": "tester"
    })
    assert response_crear.status_code == 200
    servicio_id = response_crear.json()["id"]

    # Inactivar
    response_inactivar = client.patch(f"/api/v1/servicios/{servicio_id}/inactivar")
    assert response_inactivar.status_code == 200
    assert response_inactivar.json()["activo"] == False
