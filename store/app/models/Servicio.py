from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from datetime import datetime
from app.core.database import Base

class Servicio(Base):
    __tablename__ = "servicios"

    id = Column(Integer, primary_key=True, index=True)
    codigo_interno = Column(String(20), unique=True, nullable=False)
    descripcion = Column(String(255), nullable=False)
    valor_total = Column(Float, nullable=False)
    temporal = Column(Boolean, default=False)
    creado_por = Column(String(50), nullable=True)  # Usuario que lo registró
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    activo = Column(Boolean, default=True)
