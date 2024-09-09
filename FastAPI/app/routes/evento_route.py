from fastapi import APIRouter, Body
from models.evento import Evento
from database import EventoModel 

evento_route = APIRouter()

@evento_route.get("/eventos")
def get_eventos():
    # Lógica para obtener y devolver todos los eventos
    return list(EventoModel.select())

@evento_route.get("/eventos/{evento_id}")
def get_evento(evento_id: int):
    # Lógica para obtener y devolver un evento específico por ID
    return EventoModel.get(EventoModel.id == evento_id)

@evento_route.post("/eventos")
def create_evento(evento: Evento = Body(...)):
    nuevo_evento = EventoModel.create(
        nombre=evento.nombre, 
        fecha=evento.fecha, 
        ubicacion=evento.ubicacion, 
        organizador=evento.organizador, 
        capacidad=evento.capacidad
    )
    return nuevo_evento

@evento_route.put("/eventos/{evento_id}")
def update_evento(evento_id: int, evento_data: dict):
    EventoModel.update(**evento_data).where(EventoModel.id == evento_id).execute()
    return {"message": "Evento actualizado"}

@evento_route.delete("/eventos/{evento_id}")
def delete_evento(evento_id: int):
    EventoModel.delete().where(EventoModel.id == evento_id).execute()
    return {"message": "Evento eliminado"}
