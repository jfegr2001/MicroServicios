from fastapi import APIRouter, Body
from models.vehiculo import Vehiculo
from database import VehiculoModel

vehiculo_route = APIRouter()

@vehiculo_route.get("/vehiculos")
def get_vehiculos():
    return list(VehiculoModel.select())

@vehiculo_route.get("/vehiculos/{matricula}")
def get_vehiculo(matricula: str):
    return VehiculoModel.get(VehiculoModel.matricula == matricula)

@vehiculo_route.post("/vehiculos")
def create_vehiculo(vehiculo: Vehiculo = Body(...)):
    nuevo_vehiculo = VehiculoModel.create(
        marca=vehiculo.marca,
        modelo=vehiculo.modelo,
        cilindraje=vehiculo.cilindraje,
        color=vehiculo.color,
        matricula=vehiculo.matricula
    )
    return nuevo_vehiculo

@vehiculo_route.put("/vehiculos/{matricula}")
def update_vehiculo(matricula: str, vehiculo_data: dict):
    VehiculoModel.update(**vehiculo_data).where(VehiculoModel.matricula == matricula).execute()
    return {"message": "Vehículo actualizado"}

@vehiculo_route.delete("/vehiculos/{matricula}")
def delete_vehiculo(matricula: str):
    VehiculoModel.delete().where(VehiculoModel.matricula == matricula).execute()
    return {"message": "Vehículo eliminado"}
