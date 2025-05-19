# 📦 Tienda de Maquillaje

## 🚀 Descripción

Backend moderno para gestión de inventario, facturación y cuadre de caja diseñado específicamente para tiendas de maquillaje, desarrollado con:

- **FastAPI** (Framework web moderno y rápido)
- **MySQL** (Base de datos relacional robusta)
- **SQLAlchemy** (ORM para manejo de base de datos)
- **JWT** (Autenticación segura)

## 🌟 Características Principales

✔️ Gestión completa de inventario  
✔️ Sistema de facturación integrado  
✔️ Cuadre de caja automatizado  
✔️ Generación de reportes  
✔️ Autenticación por roles (Admin, Caja, Soporte)  
✔️ Documentación API interactiva incluida  

## 🛠️ Tecnologías

**Backend**:
- Python 3.9+
- FastAPI
- Uvicorn (Servidor ASGI)

**Base de Datos**:
- MySQL 8.0+
- SQLAlchemy ORM
- Alembic (Para migraciones)

**Autenticación**:
- JWT (JSON Web Tokens)
- OAuth2 con Password Flow

## 📂 Estructura del Proyecto

```
Store/
├── app/
│   ├── core/                # Configuraciones centrales
│   ├── models/              # Modelos de base de datos
│   ├── schemas/             # Esquemas Pydantic
│   ├── api/                 # Endpoints API
│   │   ├── v1/              # Versión 1 de la API
│   │   │   ├── endpoints/   # Todos los endpoints
│   │   │   └── api.py       # Router principal
│   ├── crud/                # Operaciones de base de datos
│   ├── services/            # Lógica de negocio
│   ├── utils/               # Utilidades comunes
│   └── main.py              # App principal
├── migrations/              # Migraciones de base de datos
├── tests/                   # Pruebas automatizadas
├── requirements.txt         # Dependencias
├── .env                     # Variables de entorno
└── README.md                # Descripcion del Proyecto
```

## 🚀 Primeros Pasos

### Prerrequisitos

- Python 3.9+
- MySQL 8.0+ instalado y corriendo
- Credenciales de acceso a MySQL

### 1. Configuración Inicial

```bash
# Clonar repositorio
git clone [url-del-repositorio]
cd Store

# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Configurar Variables de Entorno

Crear archivo `.env` en la raíz:

```ini
# Database
DB_HOST=localhost
DB_PORT=3306
DB_USER=usuario_mysql
DB_PASS=contraseña_segura
DB_NAME=Store

# Security
SECRET_KEY=clave-secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# App
DEBUG=True
```

### 3. Configurar Base de Datos MySQL

```sql
CREATE DATABASE Store CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER 'usuario_mysql'@'localhost' IDENTIFIED BY 'contraseña_segura';
GRANT ALL PRIVILEGES ON Store.* TO 'usuario_mysql'@'localhost';
FLUSH PRIVILEGES;
```

### 4. Ejecutar Migraciones

```bash
alembic upgrade head
```

### 5. Crear Usuario Admin Inicial

```bash
python -m app.utils.create_admin
```

### 6. Iniciar Servidor

```bash
uvicorn app.main:app --reload
```

La aplicación estará disponible en:  
http://localhost:8000

## 📚 Documentación de la API

FastAPI genera automáticamente documentación interactiva:

- **Swagger UI**: http://localhost:8000/docs  
- **ReDoc**: http://localhost:8000/redoc  

## 🔐 Autenticación

El sistema usa JWT para autenticación. Ejemplo de flujo:

1. **Login** (`POST /api/v1/auth/login`):
```json
{
  "username": "admin",
  "password": "admin123"
}
```

2. **Usar token en requests**:
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsIn...
```

## 🌐 Endpoints Principales

| Módulo         | Endpoint                     | Método | Descripción                  |
|----------------|------------------------------|--------|------------------------------|
| Autenticación  | `/api/v1/auth/login`         | POST   | Iniciar sesión               |
| Usuarios       | `/api/v1/usuarios/`          | POST   | Crear usuario                |
| Productos      | `/api/v1/productos/`         | GET    | Listar productos             |
| Productos      | `/api/v1/productos/`         | POST   | Crear producto               |
| Inventario     | `/api/v1/inventario/stock`   | PATCH  | Actualizar stock             |
| Facturación    | `/api/v1/facturas/`          | POST   | Crear factura                |
| Reportes       | `/api/v1/reportes/ventas`    | GET    | Generar reporte de ventas    |

## 🧪 Ejecutar Pruebas

```bash
pytest tests/
```

## 🐳 Docker (Opcional)

```bash
docker-compose up --build
```

## 🚀 Despliegue en Producción

Recomendaciones:
- Usar **Gunicorn** + **Uvicorn** para producción
- Configurar **HTTPS** con certificado SSL
- Implementar **backups** automáticos de MySQL
- Usar **Redis** para caché

Ejemplo con Gunicorn:
```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
```

## 🤝 Contribuir

1. Asegúrate de estar en la rama `dev` y actualízala:
   `git checkout dev`
   `git pull origin dev`
2. Crea una nueva rama para tu módulo (`git checkout -b feature/nuevo-modulo`)
3. Guarda tus cambios y haz commit
   `git add .`
   `git commit -m "Módulo <nombre> listo para revisión"`
4. Haz push a la rama (`git push origin feature/nuevo-modulo`)
5. Abre un Pull Request desde GitHub:

    Ve al repositorio en GitHub.
    Te aparecerá un botón para comparar y abrir un PR automáticamente (si no, ve a la pestaña "Pull requests" y haz clic en "New pull request").
    Base: selecciona la rama dev.
    Compare: selecciona tu rama feature/nuevo-modulo.
    Título sugerido: "Módulo <nombre> listo para revisión".
    Añade una breve descripción de lo que hiciste.
    Haz clic en "Create pull request".

**Nota:** Puedes consultar mas para contribuir en [GUIA_BACKEND](GUIA_BACKEND.md)

## 📄 Licencia

MIT License - Ver [LICENSE](LICENSE) para detalles.
