from app.core.database import Base, engine
from app.models.Servicio import Servicio  # importa todos tus modelos aquí

print("Creando tablas en la base de datos MySQL...")
Base.metadata.create_all(bind=engine)
print("Listo.")
