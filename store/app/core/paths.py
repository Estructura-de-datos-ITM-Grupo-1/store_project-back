import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# data/
DATA_DIR = os.path.join(BASE_DIR, "data")

SERVICIOS_JSON = os.path.abspath(os.path.join(DATA_DIR, "servicios.json"))
CLIENTES_JSON = os.path.abspath(os.path.join(DATA_DIR, "clientes.json"))
USUARIOS_JSON = os.path.abspath(os.path.join(DATA_DIR, "usuarios.json"))
AUDITORIA_CLIENTES_JSON = os.path.abspath(os.path.join(DATA_DIR, "auditoria_clientes.json"))
CUADRE_CAJA_JSON = os.path.abspath(os.path.join(DATA_DIR, "cuadre_caja.json"))
INVENTARIO_JSON = os.path.abspath(os.path.join(DATA_DIR, "inventario_data.json"))
MOVIMIENTOS_JSON = os.path.abspath(os.path.join(DATA_DIR, "inventario_movimientos_data.json"))
FACTURAS_JSON = os.path.abspath(os.path.join(DATA_DIR, "facturas.json"))