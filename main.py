from fastapi import FastAPI
import uvicorn
from routes.events import event
from config.database import engine, Base, session
from schemas.events import EventType, EventStatus, EventManagement
from models.events import Event

app = FastAPI(title="CRUD EVENTOS")
app.include_router(event)

if __name__ == "__main__":
    # Eliminar las tablas
    #Base.metadata.drop_all(engine)
    # Creacion de las tablas
    Base.metadata.create_all(engine)

    example_events = [
        {
            "tipo_evento": EventType.tipo_1,
            "descripcion": "Descripción del Evento 1",
            "estado": EventStatus.pendiente,
            "fecha": "2023-07-30 14:02:50",
            "gestion": EventManagement.req_gestion
        },
        {
            "tipo_evento": EventType.tipo_2,
            "descripcion": "Descripción del Evento 2",
            "estado": EventStatus.revisado,
            "fecha": "2023-06-30 14:02:50",
            "gestion": EventManagement.sin_gestion
        },
        {
            "tipo_evento": EventType.tipo_3,
            "descripcion": "Descripción del Evento 3",
            "estado": EventStatus.revisado,
            "fecha": "2023-08-03 20:15:26",
            "gestion": EventManagement.req_gestion
        },
        {
            "tipo_evento": EventType.tipo_2,
            "descripcion": "Descripción del Evento 4",
            "estado": EventStatus.pendiente,
            "fecha": "2023-08-15 05:02:50",
            "gestion": EventManagement.sin_gestion
        },
        {
            "tipo_evento": EventType.tipo_3,
            "descripcion": "Descripción del Evento 5",
            "estado": EventStatus.revisado,
            "fecha": "2023-07-25 14:02:50",
            "gestion": EventManagement.req_gestion
        }
    ]
    for example in example_events:
        event = Event(**example)
        session.add(event)

    session.commit()
    session.close()
    # inicio del servidor
    uvicorn.run("main:app", port=5000, reload=True, log_level="info")
    