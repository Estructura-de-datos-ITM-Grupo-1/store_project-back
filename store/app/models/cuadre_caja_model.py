from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from store.app.core.paths import Base

def utc_now():
    return datetime.now(timezone.utc)

class CuadreCaja(Base):
    __tablename__ = "cuadre_caja"
    
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime(timezone=True), nullable=False, default=utc_now)
    usuario = Column(String, nullable=False)
    base_caja = Column(Float, nullable=False)
    total_ingresos = Column(Float, nullable=False)
    total_egresos = Column(Float, nullable=False)
    utilidad = Column(Float, nullable=False)
    comentario = Column(String, nullable=True)

