from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from datetime import datetime
from app.core.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    
    nombre_usuario = Column(Integer, primary_key=True, index=True)
    nombre_completo = Column(String, nullable=False)
    contrasena = Column(Float, nullable=False)
    correo = Column(Float, nullable=False)
    rol = Column(Float, nullable=False)
    activo = Column(Boolean, default=True)