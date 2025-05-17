
# 👨‍💻 Guía para responsables del Backend

📦 **Repositorio oficial**:  
🔗 [store_project-back](https://github.com/Estructura-de-datos-ITM-Grupo-1/store_project-back.git)

### 🧩 Estructura de ramas

- **main**: Rama estable y final del proyecto. Solo se actualiza con versiones aprobadas.
- **dev**: Rama de integración común para pruebas y validaciones.
- **feature/<modulo>**: Ramas personales para el desarrollo de cada módulo (cada desarrollador crea su rama).

### ✅ Pasos para trabajar correctamente

#### 1️⃣ Clonar el repositorio

Primero, clona el repositorio en tu máquina local. Abre la terminal y ejecuta los siguientes comandos:

```bash
git clone https://github.com/Estructura-de-datos-ITM-Grupo-1/store_project-back.git
cd store_project-back
````

#### 2️⃣ Cambiar a la rama `dev`

Para asegurarte de estar trabajando sobre la rama correcta, cambia a la rama `dev` (si no la tienes localmente, la creamos). Ejecuta:

```bash
git checkout dev
```

Si recibes un error diciendo que no existe la rama `dev` localmente, ejecuta los siguientes comandos para obtenerla desde el repositorio remoto:

```bash
git fetch origin
git checkout -b dev origin/dev
```

#### 3️⃣ Crear tu rama de trabajo

Ahora, crea una rama nueva basada en `dev` para desarrollar tu módulo. Reemplaza `tu-modulo` por el nombre de tu módulo (por ejemplo, `clientes`, `facturacion`, etc.).

```bash
git checkout -b feature/tu-modulo
git push -u origin feature/tu-modulo
```

**Ejemplo:**
Si estás trabajando en el módulo "clientes", el comando sería:

```bash
git checkout -b feature/clientes
git push -u origin feature/clientes
```

#### 4️⃣ Desarrollar tu módulo

Ya en tu rama, comienza a desarrollar tu módulo siguiendo la estructura esperada del proyecto:

* `models/`: (opcional) si defines estructuras internas
* `schemas/`: Esquemas de validación con Pydantic
* `routes/` o `routers/`: Endpoints de FastAPI
* `services/`: Lógica de negocio y acceso a datos desde archivos .json, .csv, etc. ✅ ACTUALIZADO
* `data/`: Aquí puedes guardar archivos como clientes.json, facturacion.csv, etc. ✅ NUEVO

Para ejecutar el proyecto localmente, usa:

```bash
uvicorn app.main:app --reload
```

#### 5️⃣ Haz commits frecuentemente

Asegúrate de hacer commits frecuentemente para guardar tus avances. Para hacerlo:

```bash
git add .
git commit -m "Avance en módulo <tu-modulo>"
git push
```

Reemplaza `<tu-modulo>` por el nombre del módulo en el que estás trabajando, por ejemplo: `"Avance en módulo clientes"`.

#### 6️⃣ Finaliza tu trabajo con un Pull Request (PR)

Cuando hayas terminado tu módulo, crea un Pull Request (PR) hacia la rama `dev`. Para hacerlo:

1. Entra al repositorio en GitHub.
2. Cambia a tu rama `feature/tu-modulo`.
3. Haz clic en **"Compare & pull request"**.
4. Verifica que la base del PR esté apuntando a la rama `dev`.
5. Título sugerido del PR: `"Módulo <tu-modulo> listo para revisión"`.
6. Envía el PR.

#### 7️⃣ Cargar y leer los datos locales

Si tu módulo necesita leer información, hazlo cargando los archivos desde la carpeta `Store/data/` usando funciones en `services/`.

Ejemplo:

```python
import json
def cargar_clientes():
    with open("Store/data/clientes.json", "r") as f:
        return json.load(f)
```

### 👥 Asignación de módulos y ramas

| Integrante | Módulo            | Rama                |
| ---------- | ----------------- | ------------------- |
| Persona 1  | Clientes          | feature/clientes    |
| Persona 2  | Servicios         | feature/servicios   |
| Persona 3  | Inventario        | feature/inventario  |
| Persona 4  | Facturación       | feature/facturacion |
| Persona 5  | Cuadre de Caja    | feature/caja        |
| Persona 6  | Reportes          | feature/reportes    |
| Persona 7  | Usuarios y Config | feature/usuarios    |

---

### 📌 Reglas clave del equipo

* 🚫 **No se trabaja directamente en `main`**.
* ✅ **Solo se hace merge a `dev` desde ramas `feature/...` con funcionalidad comprobada**.
* 🧹 **Mantén el código modular y ordenado**.
* 🧪 **Prueba cada endpoint en Swagger antes de hacer un PR**.

### 📣 ¿Dudas o bloqueos?

Si tienes alguna duda o te encuentras bloqueado, contacta al líder técnico o al integrador del proyecto.

