import json
import uuid
from datetime import datetime
from app.schemas.facturacion_schema import FacturaCrear, FacturaRespuesta
from app.core.paths import FACTURAS_JSON


def leer_facturas():
    try:
        with open(FACTURAS_JSON, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def escribir_facturas(data):
    with open(FACTURAS_JSON, "w") as f:
        json.dump(data, f, indent=4)

def crear_factura(factura: FacturaCrear) -> FacturaRespuesta:
    facturas = leer_facturas()
    nueva = factura.dict()
    nueva["id"] = str(uuid.uuid4())
    nueva["fecha"] = datetime.now().isoformat()
    facturas.append(nueva)
    escribir_facturas(facturas)
    return FacturaRespuesta(**nueva)

def obtener_facturas():
    return leer_facturas()