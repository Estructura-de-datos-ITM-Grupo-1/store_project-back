
# 👨‍💻 Guía para responsables del Backend

📦 Repositorio oficial:  
🔗 https://github.com/Estructura-de-datos-ITM-Grupo-1/store_project-back.git

---

## 🧩 Estructura de ramas

- `main`: rama estable y final del proyecto. Solo se actualiza con versiones aprobadas.
- `dev`: rama de integración común para pruebas y validaciones.
- `feature/<modulo>`: ramas personales para el desarrollo de cada módulo.

---

## ✅ Pasos para trabajar correctamente

### 1️⃣ Clona el repositorio

```bash
git clone https://github.com/Estructura-de-datos-ITM-Grupo-1/store_project-back.git
cd store_project-back
```

---

### 2️⃣ Cambia a la rama `dev`

```bash
git checkout dev
```

Si no tienes la rama `dev` local:

```bash
git fetch origin
git checkout -b dev origin/dev
```

---

### 3️⃣ Crea tu rama de trabajo

Reemplaza `tu-modulo` por el nombre real de tu módulo (ej. `clientes`, `caja`, `facturacion`):

```bash
git checkout -b feature/tu-modulo
git push -u origin feature/tu-modulo
```

---

### 4️⃣ Desarrolla tu módulo

📌 Estructura esperada:

- Modelos: `/models/`
- Esquemas: `/schemas/`
- Rutas: `/routes/` o `/routers/`
- Servicios: `/services/` (si aplica)

🧪 Ejecuta localmente con:

```bash
uvicorn app.main:app --reload
```

Haz commits frecuentemente:

```bash
git add .
git commit -m "Avance en módulo <tu-modulo>"
git push
```

---

### 5️⃣ Finaliza tu trabajo con un Pull Request (PR)

1. Entra al [repositorio](https://github.com/Estructura-de-datos-ITM-Grupo-1/store_project-back)
2. Cambia a tu rama `feature/tu-modulo`
3. Haz clic en **"Compare & pull request"**
4. Verifica que sea hacia `dev`
5. Título sugerido: `"Módulo clientes listo para revisión"`
6. Enviar PR

---

### 6️⃣ Crea las tablas localmente (una vez tengas modelos nuevos)

```bash
python create_tables.py
```

Esto generará el archivo `tienda.db` con todas las tablas actualizadas.

---

## 👥 Asignación de módulos y ramas

| Integrante  | Módulo            | Rama                       |
|-------------|-------------------|----------------------------|
| Persona 1   | Clientes           | `feature/clientes`         |
| Persona 2   | Servicios          | `feature/servicios`        |
| Persona 3   | Inventario         | `feature/inventario`       |
| Persona 4   | Facturación        | `feature/facturacion`      |
| Persona 5   | Cuadre de Caja     | `feature/caja`             |
| Persona 6   | Reportes           | `feature/reportes`         |
| Persona 7   | Usuarios / Config  | `feature/usuarios`         |

---

## 📌 Reglas clave del equipo

- 🚫 **No se trabaja directamente en `main`**
- ✅ Solo se hace merge a `dev` desde ramas `feature/...` con funcionalidad comprobada
- 🧹 Mantén el código modular y ordenado
- 🧪 Prueba cada endpoint en Swagger antes de hacer un PR

---

📣 **¿Dudas o bloqueos?**  
Contacta al líder técnico o integrador del proyecto.
