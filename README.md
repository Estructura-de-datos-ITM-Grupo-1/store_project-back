# Proyecto Backend con FastAPI, Uvicorn y ReactPy

Este proyecto está desarrollado en **Python** y utiliza las siguientes tecnologías clave:

- **FastAPI**
- **Uvicorn**
- **ReactPy**

A continuación, se detallan las funciones de cada tecnología, cómo instalarlas y cómo ejecutar el proyecto.

---

## 📦 Tecnologías utilizadas

### 🌀 FastAPI
FastAPI es un moderno y eficiente framework web para construir APIs con Python. Su principal ventaja es la rapidez para desarrollar y su compatibilidad con tipado estático, validación automática de datos y documentación interactiva con Swagger.

En este proyecto, **FastAPI** se utiliza para definir las rutas de la aplicación, manejar la lógica del backend y exponer endpoints de forma sencilla.

### ⚡ Uvicorn
Uvicorn es un servidor ASGI (Asynchronous Server Gateway Interface) rápido y ligero, ideal para correr aplicaciones hechas con FastAPI. Es compatible con características modernas como WebSockets y HTTP/2.

En este proyecto, **Uvicorn** se encarga de ejecutar la aplicación FastAPI, permitiendo que esté disponible como un servidor web.

### 🧩 ReactPy
ReactPy (anteriormente llamado IDOM) permite crear interfaces de usuario reactivas directamente desde Python. Con esta herramienta puedes construir componentes similares a React, pero sin necesidad de escribir JavaScript.

En este proyecto, **ReactPy** se utiliza para construir una interfaz dinámica directamente desde el backend con Python, integrándose fácilmente con FastAPI.

---

## ✅ Requisitos previos

- Python 3.8 o superior
- pip (el gestor de paquetes de Python)

---

## ⚙️ Instalación del entorno

para instalar las dependencias del proyecto se realizan los siguientes pasos

- cd backend
- pip install reactpy[fastapi]
- pip install uvicorn[standard]


## Ejecución del backend

Para ejecutar el backend se tiene que usar el siguiente comando

- uvicorn app.modules.main:app --reload
