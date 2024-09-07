from pydantic import BaseModel

class Vehiculo(BaseModel):
    marca: str
    modelo: str
    cilindraje: int
    color: str
    matricula: str
