import json
from pathlib import Path
from typing import List, Dict

DATA_FILE = Path(__file__).parent.parent / "data" / "productos.json"

def cargar_productos() -> List[Dict]:
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_productos(productos: List[Dict]):
    DATA_FILE.parent.mkdir(exist_ok=True)
    with open(DATA_FILE, "w") as file:
        json.dump(productos, file, indent=4)
    