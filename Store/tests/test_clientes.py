import os
import json
import shutil
import pytest
from app.services import clientes_service as cs

# Rutas de prueba
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'test_data')
TEST_CLIENTES = os.path.join(TEST_DATA_DIR, 'clientes.json')
TEST_AUDITORIA = os.path.join(TEST_DATA_DIR, 'auditoria_clientes.json')

# Fixture para preparar entorno de pruebas
@pytest.fixture(autouse=True)
def setup_archivos(monkeypatch):
    # Crear carpeta temporal
    if not os.path.exists(TEST_DATA_DIR):
        os.makedirs(TEST_DATA_DIR)

    # Inicializar archivos vacíos
    with open(TEST_CLIENTES, 'w', encoding='utf-8') as f:
        json.dump([], f)
    with open(TEST_AUDITORIA, 'w', encoding='utf-8') as f:
        json.dump([], f)

    # Monkeypatch para redirigir los archivos a test_data
    monkeypatch.setattr(cs, 'ARCHIVO_CLIENTES', TEST_CLIENTES)
    monkeypatch.setattr(cs, 'ARCHIVO_AUDITORIA', TEST_AUDITORIA)

    yield

    # Limpieza después del test
    shutil.rmtree(TEST_DATA_DIR)


def test_registrar_cliente():
    cliente = cs.registrar_cliente(
        rol='administrador',
        nombre='Juan Pérez',
        tipo_id='CC',
        numero_id='123456',
        telefono='5551234',
        email='juan@mail.com',
        direccion='Calle Falsa 123'
    )
    assert cliente['id'] == '1'
    assert cliente['estado'] == 'activo'
    assert cliente['nombre'] == 'Juan Pérez'


def test_listar_clientes_activos():
    cs.registrar_cliente('administrador', 'Maria', 'CC', '456', '1234', 'maria@mail.com', 'Cra 45')
    activos = cs.listar_clientes_activos()
    assert len(activos) == 1
    assert activos[0]['nombre'] == 'Maria'


def test_modificar_cliente():
    cs.registrar_cliente('administrador', 'Carlos', 'CC', '789', '0000', 'carlos@mail.com', 'Calle Luna')
    modificado = cs.modificar_cliente('administrador', '1', 'telefono', '9999')
    assert modificado['telefono'] == '9999'


def test_inactivar_cliente():
    cs.registrar_cliente('administrador', 'Laura', 'CC', '321', '1111', 'laura@mail.com', 'Cra Sol')
    inactivado = cs.inactivar_cliente('administrador', '1')
    assert inactivado['estado'] == 'inactivo'
    activos = cs.listar_clientes_activos()
    assert len(activos) == 0


def test_error_rol_no_autorizado():
    with pytest.raises(PermissionError):
        cs.registrar_cliente('visitante', 'No válido', 'CC', '000', '0000', 'x@mail.com', 'null')


def test_modificar_cliente_inexistente():
    with pytest.raises(ValueError):
        cs.modificar_cliente('administrador', '999', 'telefono', '0000')


def test_inactivar_cliente_ya_inactivo():
    cs.registrar_cliente('administrador', 'Ana', 'CC', '111', '1111', 'ana@mail.com', 'Calle 1')
    cs.inactivar_cliente('administrador', '1')
    with pytest.raises(ValueError):
        cs.inactivar_cliente('administrador', '1')
