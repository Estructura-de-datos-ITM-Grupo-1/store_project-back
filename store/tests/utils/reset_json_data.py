import os
import json

def reset_servicios_json():
    path = os.path.join(os.path.dirname(__file__), "../../app/data/servicios.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump([], f)
