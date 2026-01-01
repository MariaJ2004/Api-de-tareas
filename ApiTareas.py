from fastapi import *
from pydantic import BaseModel,Field
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError

app=FastAPI()

class Task(BaseModel):
   
    title: str= Field(min_length=3,max_length=300)

    description: str | None = Field(default=None, max_length=500)

    completed: bool = Field(default=False)

    priority: str= Field(pattern="^(alta|media|baja)$")

class RespuestaTareas(Task):
    id:int


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


tareas={}
id_cont=0
@app.post("/tasks",response_model=RespuestaTareas)
async def crear_tarea(tarea:Task= Body(
        openapi_examples={
            "tarea_normal": {
                "summary": "Tarea normal",
                "description": "Ejemplo de una tarea creada correctamente.",
                "value": {
                    "title": "Estudiar FastAPI",
                    "description": "Repasar Body y OpenAPI examples",
                    "completed": False,
                    "priority": "alta"
                },
            },
            "tarea_completada": {
                "summary": "Tarea completada",
                "description": "Ejemplo de una tarea ya finalizada.",
                "value": {
                    "title": "Enviar proyecto",
                    "description": "Proyecto final enviado al repositorio",
                    "completed": True,
                    "priority": "media"
                },
            },
            "tarea_sin_descripcion": {
                "summary": "Tarea sin descripción",
                "description": "La descripción es opcional.",
                "value": {
                    "title": "Leer documentación",
                    "completed": False,
                    "priority": "baja"
                },
            },
            "tarea_invalida": {
                "summary": "Datos inválidos",
                "description": "Ejemplo con tipos incorrectos (FastAPI lo rechaza).",
                "value": {
                    "title": "Romper la API",
                    "completed": "no",
                    "priority": 3
                },
            },
        }
    )):

    global id_cont
    id_cont+=1
    NuevoValor={"id":id_cont,**tarea.model_dump()}
    tareas[id_cont]=NuevoValor
    return NuevoValor

@app.get("/tasks",response_model=list[RespuestaTareas])
async def filtrar_datos(completed:bool |None=None, priority:str |None=Query(pattern="^(alta|media|baja)$")):
    resultado=list(tareas.values())
    if completed is not None and priority is not None: 
        filtrado=[tarea for tarea in resultado if tarea["completed"]==completed and tarea["priority"]==priority]

    elif completed is not None:
        filtrado=[tarea for tarea in resultado if tarea["completed"]==completed]

    elif priority is not None:
        filtrado=[tarea for tarea in resultado if tarea["priority"]==priority]
        
    else:
        filtrado= resultado

    return filtrado


@app.get("/tasks/{id}",response_model=RespuestaTareas)
async def filtrar_id(id:int):
    if id not in tareas:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tareas[id]


@app.put("/tasks/{id}",response_model=RespuestaTareas)
async def actualizar_tarea(id:int,datosActualizados:Task):
    if id not in tareas:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    tarea_actualizada = {"id": id, **datosActualizados.model_dump()}
    tareas[id] = tarea_actualizada
    return tarea_actualizada



@app.delete("/tasks/{id}")
async def eliminar_tarea(id:int):
    if id not in tareas:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    del tareas[id]
    

