
# 👨‍💻 Guía para colaboradores del Backend

Repositorio oficial:  
🔗 https://github.com/Estructura-de-datos-ITM-Grupo-1/store_project-back.git

---

## 🧩 Estructura de ramas

- `main`: rama final y estable, solo se actualiza al final del proyecto.
- `dev`: rama común de integración de todos los módulos.
- `feature/<modulo>`: ramas individuales para cada integrante.

---

## ✅ Pasos para trabajar correctamente

### 1. Clona el repositorio

```bash
git clone https://github.com/Estructura-de-datos-ITM-Grupo-1/store_project-back.git
cd store_project-back
```

---

### 2. Cambia a la rama `dev`

```bash
git checkout dev
```

Si no tienes la rama `dev` aún:

```bash
git fetch origin
git checkout -b dev origin/dev
```

---

### 3. Crea tu rama personal desde `dev`

Reemplaza `tu-modulo` por el nombre real de tu módulo (clientes, caja, etc):

```bash
git checkout -b feature/tu-modulo
git push -u origin feature/tu-modulo
```

---

### 4. Trabaja en tu módulo

- Agrega modelo ORM en `/models/`
- Agrega schemas en `/schemas/`
- Agrega rutas en `/routers/`
- Probar localmente (`uvicorn app.main:app --reload`)

### Haz commits y push:

```bash
git add .
git commit -m "Avance en módulo <tu-modulo>"
git push
```

---

### 5. Cuando termines: Pull Request

1. Ve a [GitHub](https://github.com/Estructura-de-datos-ITM-Grupo-1/store_project-back)
2. Selecciona tu rama (ej. `feature/clientes`)
3. Haz clic en **"Compare & pull request"**
4. Asegúrate de hacer el PR hacia la rama `dev`
5. Escribe un título como: `"Módulo clientes listo para revisión"` y envía el PR

---

### 6. Crear las tablas localmente (una vez tengas modelo)

```bash
python create_tables.py
```

Esto generará el archivo `tienda.db` con las tablas correspondientes.

---

## 📋 Asignación de ramas

| Persona   | Módulo           | Rama                       |
|-----------|------------------|----------------------------|
| Persona 1 | Clientes         | `feature/clientes`         |
| Persona 2 | Servicios        | `feature/servicios`        |
| Persona 3 | Inventario       | `feature/inventario`       |
| Persona 4 | Facturación      | `feature/facturacion`      |
| Persona 5 | Cuadre de Caja   | `feature/caja`             |
| Persona 6 | Reportes         | `feature/reportes`         |
| Persona 7 | Usuarios / Config| `feature/usuarios`         |

---

## 📌 Reglas clave

- 🔒 **No trabajar nunca directamente en `main`**
- 🧪 Solo se hace `merge` a `dev` desde ramas `feature/...` con código funcional
- 🧼 Mantener el código limpio y modular
- 🧪 Probar cada endpoint en Swagger antes de enviar PR

---

Cualquier duda → preguntar al líder del equipo o integrador
