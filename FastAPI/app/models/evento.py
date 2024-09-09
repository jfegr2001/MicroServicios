from pydantic import BaseModel

class Evento(BaseModel):
    nombre: str
    fecha: str
    ubicacion: str
    organizador: str
    capacidad: int
