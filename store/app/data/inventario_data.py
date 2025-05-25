import json
from pathlib import Path


archivo_inventario = Path("inventario.json")

def cargar_productos():
    try:
        with open(archivo_inventario, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_productos(productos):
    with open(archivo_inventario, "w") as file:
        json.dump(productos, file, indent=4)
    