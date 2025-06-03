import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from app.routes.clientes_routes import router as cliente_router
from app.routes.servicio_routes import router as servicio_router
from app.routes.cuadre_caja_routes import router as cuadre_caja_router
from app.routes.usuario_routes import router as usuario_router
from app.routes.auditoria_routes import router as auditoria_router
from app.routes.inventario_routes import router as inventario_router 
from app.routes.facturacion_routes import router as facturacion_router
from app.routes.report_routes import router as report_router

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/usuarios/login")

app = FastAPI(
    title="Tienda Maquillaje API",
    description="Sistema Tienda con autenticación JWT",
    version="1.0.0",
    openapi_tags=[
        {"name": "Clientes", "description": "Gestión de clientes"},
        {"name": "Usuarios", "description": "Autenticación y gestión de usuarios"},
        {"name": "Auditoría", "description": "Seguimiento de cambios en clientes"},
        {"name": "Servicios", "description": "Gestión de servicios ofrecidos"},
        {"name": "Inventario", "description": "Gestión de productos y movimientos"},
        {"name": "Cuadre Caja", "description": "Resumen y cuadre de caja"},
        {"name": "Facturacion", "description": "Facturación y registros"},
        {"name": "Reportes", "description": "Generación y exportación de reportes"}
    ]
)

app.include_router(cliente_router, prefix="/api/v1/clientes")
app.include_router(auditoria_router, prefix="/api/v1/auditoria")
app.include_router(servicio_router, prefix="/api/v1/servicios")
app.include_router(inventario_router, prefix="/api/v1/inventario")
app.include_router(cuadre_caja_router, prefix="/api/v1/caja")
app.include_router(report_router, prefix="/api/v1/reportes")
app.include_router(facturacion_router, prefix="/api/v1/facturacion")
app.include_router(usuario_router, prefix="/api/v1/usuarios")





