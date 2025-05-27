from pydantic import BaseModel
from typing import Optional
from datetime import date

class ReportFilter(BaseModel):
    start_date: date
    end_date: date
    report_type: str  # ventas, inventario, servicios, etc.

class ReportOut(BaseModel):
    title: str
    total_items: int
    summary: dict
