import json
from pathlib import Path
from typing import List, Dict, Any

DATA_DIR = Path(__file__).parent.parent / "data"

def leer_json(nombre_archivo: str) -> List[Dict[str, Any]]:
    ruta = DATA_DIR / nombre_archivo
    if not ruta.exists():
        return []
    with open(ruta, "r", encoding="utf-8") as file:
        return json.load(file)

def escribir_json(nombre_archivo: str, datos: List[Dict[str, Any]]) -> None:
    ruta = DATA_DIR / nombre_archivo
    ruta.parent.mkdir(exist_ok=True)  # Crea la carpeta si no existe
    with open(ruta, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)