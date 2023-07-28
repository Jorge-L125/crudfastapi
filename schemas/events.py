from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum as PyEnum


class EventType(str, PyEnum):
    tipo_1 = "Evento tipo 1"
    tipo_2 = "Evento tipo 2"
    tipo_3 = "Evento tipo 3"

class EventStatus(str, PyEnum):
    pendiente = "Pendiente"
    revisado = "Revisado"

class EventManagement(str, PyEnum):
    req_gestion = "Requiere Gestión"
    sin_gestion = "Sin Gestión"

class EventManager(str, PyEnum):
    req_gestion = "management"
    sin_gestion = "notmanagement"

class Event(BaseModel):
    tipo_evento: EventType
    descripcion: str | None = None
    fecha: datetime = datetime.now()
    estado: EventStatus

class EventUpdate(BaseModel):
    tipo_evento: str | None = None
    descripcion: str | None = None
    fecha: datetime | None = None
    estado: str | None = None
    