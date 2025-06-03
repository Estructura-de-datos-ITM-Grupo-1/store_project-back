from datetime import date
from typing import Dict
from app.schemas.report_schema import ReportFilter

import csv

def generate_report(filter_data: ReportFilter) -> Dict:
    # Aquí deberías consultar la base de datos o archivos según `report_type`
    # Simulamos datos por ahora:
    report_data = {
        "ventas": {
            "total_items": 120,
            "summary": {"total_ventas": 500000, "clientes": 35}
        },
        "inventario": {
            "total_items": 230,
            "summary": {"stock_bajo": 12, "productos_totales": 230}
        }
    }
    return report_data.get(filter_data.report_type, {
        "total_items": 0,
        "summary": {"mensaje": "Tipo de reporte no válido"}
    })

def export_to_csv(data: Dict, filename: str) -> str:
    filepath = f"app/data/{filename}"
    with open(filepath, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Clave", "Valor"])
        for key, value in data["summary"].items():
            writer.writerow([key, value])
    return filepath
