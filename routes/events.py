from fastapi import APIRouter, HTTPException
from config.database import session
from models.events import Event
from schemas.events import EventUpdate, EventManagement, Event as EventSchema, EventStatus, EventManager 

event = APIRouter()

@event.get("/api/events")
def get_events():
    events = session.query(Event).order_by(Event.id.asc()).all()
    session.close()
    return events

@event.get("/api/events/{id}")
def get_event_by_id(id: int):
    event = session.query(Event).filter(Event.id == id).first()
    if not event:
        raise HTTPException(status_code=404, detail="No se encontro el evento")
    session.close()
    return event

@event.post("/api/events")
def create_event(event: EventSchema):
    management = None
    if event.tipo_evento == "Evento tipo 1" or event.tipo_evento == "Evento tipo 3":
        management = EventManagement.req_gestion
    else:
        management = EventManagement.req_gestion

    data = Event(tipo_evento=event.tipo_evento, descripcion=event.descripcion, 
                fecha=event.fecha, estado=event.estado, gestion=management)
    
    session.add(data)
    session.commit()
    session.close()

    return {"mensaje": "evento guardado exitosamente"}

@event.put("/api/events/{id}")
def update_event(id: int, update_event: EventUpdate):
    event = session.query(Event).filter(Event.id == id).first()

    if not event:
        raise HTTPException(status_code=404, detail="No se encontro el evento")

    if update_event.tipo_evento is not None:
        event.tipo_evento = update_event.tipo_evento
    if update_event.descripcion is not None:
        event.descripcion = update_event.descripcion
    if update_event.fecha is not None:
        event.fecha = update_event.fecha
    if update_event.estado is not None:
        event.estado = update_event.estado

    session.commit()
    session.close()

    return {"mensaje": "evento actualizado exitosamente"}

@event.delete("/api/events/{id}")
def delete_event(id: int):
    event = session.query(Event).filter(Event.id == id).first()
    if event is None:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    
    session.delete(event)
    session.commit()
    session.close()

    return {"mensaje": "evento eliminado exitosamente"}

@event.get("/api/events/organize/{opcion}")
def organization(opcion: EventManager):
    if opcion == 'management':
        events = session.query(Event).filter(Event.gestion == EventManagement.req_gestion).filter(Event.estado == EventStatus.revisado).all()
    else:
        events = session.query(Event).filter(Event.gestion == EventManagement.sin_gestion).filter(Event.estado == EventStatus.revisado).all()
        
    if events is None:
        raise HTTPException(status_code=404, detail="No se encontraron eventos revisados")
    
    return events