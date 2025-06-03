from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.schemas.report_schema import ReportFilter, ReportOut
from app.services.report_service import generate_report, export_to_csv


router = APIRouter(tags=["Reportes"])

@router.post("/", response_model=ReportOut)
def get_report(filtros: ReportFilter):
    data = generate_report(filtros)
    return {
        "title": f"Reporte de {filtros.report_type}",
        "total_items": data["total_items"],
        "summary": data["summary"]
    }

@router.post("/exportar-csv")
def export_csv(filtros: ReportFilter):
    data = generate_report(filtros)
    filename = f"reporte_{filtros.report_type}.csv"
    path = export_to_csv(data, filename)
    return FileResponse(path, filename=filename, media_type="text/csv")
