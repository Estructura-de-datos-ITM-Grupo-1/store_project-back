from fastapi import FastAPI
from app.routes import clientes_routes
from app.routes import cuadre_caja_routes


app = FastAPI(
    title="Gestión de Clientes",
    description="API para registrar, modificar e inactivar clientes",
    version="1.0.0"
)

# Incluir el router
app.include_router(clientes_routes.router)
app.include_router(cuadre_caja_routes.router)
# Iniciar la aplicación
