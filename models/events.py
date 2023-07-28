from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Enum
from config.database import Base
from schemas.events import EventType, EventStatus, EventManagement

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    tipo_evento = Column(Enum(EventType), nullable=False)
    descripcion = Column(String(1000))
    fecha = Column(DateTime, nullable=False)
    estado = Column(Enum(EventStatus), nullable=False)
    gestion = Column(Enum(EventManagement))   


