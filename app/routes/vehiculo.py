from fastapi import APIRouter, Body
from ..models.vehiculo import Vehiculo

vehiculos_route = APIRouter()

@vehiculos_route.get("/")
async def get_vehiculo():
    try:
        return {"message": "Vehicle data"}
    except Exception as e:
        return {"error": str(e)}

@vehiculos_route.post("/")
async def post_vehiculo(vehiculo: Vehiculo = Body(...)):
    try:
        return {"message": "Vehicle created"}
    except Exception as e:
        return {"error": str(e)}
