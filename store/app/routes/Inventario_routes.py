from fastapi import APIRouter, HTTPException
from ..services import producto_service
from ..schemas.Inventario_schemas import ProductoCreate, ProductoOut

router = APIRouter(prefix="/inventario", tags=["Inventario"])

@router.post("/productos", response_model=ProductoOut, status_code=201)
def crear_producto(producto: ProductoCreate):
    try:
        return producto_service.crear_producto(producto.dict())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/productos/{codigo}", response_model=ProductoOut)
def buscar_producto(codigo: str):
    producto = producto_service.buscar_por_codigo(codigo)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.get("/productos", response_model=List[ProductoOut])
def listar_productos():
    return producto_service.obtener_todos()

@router.put("/productos/{id}", response_model=ProductoOut)
def actualizar_producto(id: int, producto: ProductoUpdate):
    try:
        return producto_service.actualizar_producto(id, producto.dict())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))