from fastapi import APIRouter, Body
from models.evento import Evento

eventos_route = APIRouter()

@eventos_route.get("/")
async def get_evento():
    try:
        return {"message": "Event data"}
    except Exception as e:
        return {"error": str(e)}

@eventos_route.post("/")
async def post_evento(evento: Evento = Body(...)):
    try:
        return {"message": "Event created"}
    except Exception as e:
        return {"error": str(e)}
