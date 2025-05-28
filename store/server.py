import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from app.routes.cliente_routes import router as cliente_router
from app.routes.servicio_routes import router as servicio_router
from app.routes.caja_routes import router as caja_router

app = FastAPI(
    title="Equipo Caja API",
    description="API para gestión de tienda",
    version="1.0.0"
)

app.include_router(cliente_router, prefix="/api/v1/clientes")
app.include_router(servicio_router, prefix="/api/v1/servicios")
app.include_router(caja_router, prefix="/api/v1/caja")