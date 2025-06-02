import os

# Directorio base del proyecto (donde está la carpeta app/)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Carpeta data/
DATA_DIR = os.path.join(BASE_DIR, "data")

# Rutas absolutas a cada archivo JSON
SERVICIOS_JSON = os.path.abspath(os.path.join(DATA_DIR, "servicios.json"))
#CLIENTES_JSON = os.path.abspath(os.path.join(DATA_DIR, "clientes.json"))
USUARIOS_JSON = os.path.abspath(os.path.join(DATA_DIR, "usuarios.json"))
#AUDITORIA_CLIENTES_JSON = os.path.abspath(os.path.join(DATA_DIR, "auditoria_clientes.json"))
CUADRE_CAJA_JSON = os.path.abspath(os.path.join(DATA_DIR, "cuadre_caja.json"))
