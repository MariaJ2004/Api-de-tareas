# FastAPI Tasks API

Esta es una **API REST básica** desarrollada con **FastAPI** como proyecto de portafolio. Su objetivo es mostrar el funcionamiento de una API sencilla para la gestión de tareas, aplicando validación de datos, manejo de errores y documentación automática.

La API trabaja con un **almacenamiento en memoria**, por lo que no utiliza base de datos. Esto permite centrarse en la lógica de los endpoints y en el flujo de datos.

---

## ¿Cómo funciona la API?

La API gestiona tareas mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar).  
Cada tarea contiene la siguiente información:

- **title**: título de la tarea  
- **description**: descripción opcional  
- **completed**: indica si la tarea está completada  
- **priority**: prioridad de la tarea (`alta`, `media` o `baja`)  
- **id**: identificador único asignado automáticamente  

Las tareas se guardan temporalmente en memoria mientras el servidor está en ejecución.

---

## Endpoints disponibles

### Crear una tarea
**POST** `/tasks`  
Crea una nueva tarea y asigna automáticamente un `id`.

### Listar tareas
**GET** `/tasks`  
Devuelve todas las tareas almacenadas.  
Permite filtrar por:
- `completed`
- `priority`

### Obtener tarea por ID
**GET** `/tasks/{id}`  
Devuelve una tarea específica según su identificador.

### Actualizar una tarea
**PUT** `/tasks/{id}`  
Actualiza completamente una tarea existente.

### Eliminar una tarea
**DELETE** `/tasks/{id}`  
Elimina una tarea por su identificador.

---

## Tecnologías utilizadas

- Python 3
- FastAPI
- Pydantic
- Uvicorn

---

## Cómo ejecutar el proyecto

```bash
pip install -r requirements.txt
uvicorn main:app --reload

