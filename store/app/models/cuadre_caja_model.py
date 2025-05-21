from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from datetime import datetime
from app.core.database import Base

class CuadreCaja(Base):
    __tablename__ = "cuadre_caja"
    
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime, nullable=False)
    usuario = Column(String, nullable=False)
    base_caja = Column(Float, nullable=False)
    total_ingresos = Column(Float, nullable=False)
    total_egresos = Column(Float, nullable=False)
    utilidad = Column(Float, nullable=False)
    comentario = Column(String, nullable=True)

