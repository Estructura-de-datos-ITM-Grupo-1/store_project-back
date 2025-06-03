from pydantic import BaseModel
from typing import Optional, Dict, Union
from datetime import date

class ReportFilter(BaseModel):
    start_date: date
    end_date: date
    report_type: str  # ventas, inventario, servicios, etc.

class ReportOut(BaseModel):
    title: str
    total_items: int
    summary: Dict[str, Union[str, int, float]]
