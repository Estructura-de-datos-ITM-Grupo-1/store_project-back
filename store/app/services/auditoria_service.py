import json
from datetime import datetime
from app.schemas.auditoria_schema import RegistroAuditoria
from app.core.paths import AUDITORIA_CLIENTES_JSON as DATA_FILE


def registrar_evento(cliente_id: int, accion: str, usuario: str, detalles: str = ""):
    evento = RegistroAuditoria(
        cliente_id=cliente_id,
        accion=accion,
        usuario=usuario,
        fecha=datetime.now(),
        detalles=detalles
    )

    try:
        with open(DATA_FILE, "r") as f:
            auditoria_data = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        auditoria_data = []

    auditoria_data.append(evento.dict())

    with open(DATA_FILE, "w") as f:
        json.dump(auditoria_data, f, indent=4, default=str)


def listar_auditoria():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []
