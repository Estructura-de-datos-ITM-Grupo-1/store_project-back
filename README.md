# 📦 Tienda de Maquillaje

## 🚀 Descripción

Backend ligero y moderno para gestión de inventario, facturación y cuadre de caja diseñado para tiendas de maquillaje, desarrollado con:

- **FastAPI** (Framework web moderno y rápido)
- **Almacenamiento en archivos JSON/CSV** (estructura simple para persistencia)
- **JWT** (Autenticación segura)

## 🌟 Características Principales

✔️ Gestión de productos desde archivos JSON/CSV  
✔️ Facturación con datos persistentes en archivos  
✔️ Cuadre de caja sin necesidad de motor de base de datos  
✔️ Autenticación por roles (Admin, Caja, Soporte)  
✔️ Documentación API interactiva incluida  

## 🛠️ Tecnologías

**Backend**:
- Python 3.9+
- FastAPI
- Uvicorn (Servidor ASGI)

**Persistencia**:
- Archivos `.json` y `.csv` como fuente de datos

**Autenticación**:
- JWT (JSON Web Tokens)
- OAuth2 con Password Flow

## 📂 Estructura del Proyecto

```

Store/
├── app/
│   ├── core/                # Configuraciones centrales
│   ├── models/              # Modelos internos (no ORM)
│   ├── schemas/             # Esquemas Pydantic
│   ├── routes/              # Endpoints API
│   ├── services/            # Lógica de negocio
│   ├── data/                # Archivos .json o .csv de persistencia
│   └── main.py              # App principal
├── tests/                   # Pruebas automatizadas
├── requirements.txt         # Dependencias
├── README.md                # Descripción del Proyecto

````

## 🚀 Primeros Pasos

### 1. Clonar y preparar entorno

```bash
git clone [url-del-repositorio]
cd store_project-back
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
````

### 2. Estructura de Archivos

Los datos se guardan en el directorio `Store/app/data/`. Asegúrate de que existan los archivos base como:

```
Store/app/data/usuarios.json
Store/app/data/servicios.json
Store/app/data/facturas.csv
```

### 3. Ejecutar servidor

```bash
uvicorn app.main:app --reload
```

Accede a la app en:
[http://localhost:8000](http://localhost:8000)

## API

* **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
* **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 🔐 Autenticación

El sistema usa JWT para autenticación. Ejemplo:

```json
POST /api/v1/auth/login
{
  "username": "admin",
  "password": "admin123"
}
```

Luego en los headers:
`Authorization: Bearer <token>`

## 🧪 Ejecutar Pruebas

```bash
pytest tests/
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
