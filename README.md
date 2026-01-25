# FastAPI Tasks API

API REST desarrollada con **FastAPI** como proyecto de práctica y portafolio.  
El proyecto muestra cómo construir una API sencilla para la gestión de tareas y cómo ejecutarla dentro de un contenedor Docker usando un Dockerfile básico.

---

## Descripción de la API

La API permite gestionar tareas mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar).

Cada tarea contiene la siguiente información:

- `id`: identificador único asignado automáticamente
- `title`: título de la tarea
- `description`: descripción opcional
- `completed`: indica si la tarea está completada
- `priority`: prioridad de la tarea (`alta`, `media`, `baja`)

Las tareas se almacenan **en memoria**, por lo que no se utiliza base de datos.  
Esto permite centrarse en la lógica de la API y en el manejo de los endpoints.

---

## Funcionalidades

- Crear nuevas tareas
- Listar todas las tareas
- Filtrar tareas por estado (`completed`) y prioridad (`priority`)
- Obtener una tarea específica por su identificador
- Actualizar tareas existentes
- Eliminar tareas

---

## Endpoints principales

- **POST** `/tasks`  
  Crea una nueva tarea.

- **GET** `/tasks`  
  Devuelve todas las tareas. Permite filtros opcionales.

- **GET** `/tasks/{id}`  
  Devuelve una tarea según su ID.

- **PUT** `/tasks/{id}`  
  Actualiza una tarea existente.

- **DELETE** `/tasks/{id}`  
  Elimina una tarea.

---

## Tecnologías utilizadas

- Python 3.11
- FastAPI
- Pydantic
- Uvicorn
- Docker

---

## Docker

El proyecto incluye un archivo `Dockerfile` que define cómo se construye la imagen Docker de la API.

### ¿Qué hace el Dockerfile?

El Dockerfile realiza los siguientes pasos:

1. Usa la imagen base `python:3.11-slim`.
2. Define `/app` como el directorio de trabajo dentro del contenedor.
3. Instala las dependencias necesarias para ejecutar la API.
4. Copia el archivo de la aplicación al contenedor.
5. Ejecuta el servidor Uvicorn exponiendo la API en el puerto 8000.

---

## Ejecutar la API con Docker

### 1️⃣ Construir la imagen

Desde la raíz del proyecto, donde se encuentra el `Dockerfile`, ejecutar:

```bash
docker build -t fastapi-tasks-api .
