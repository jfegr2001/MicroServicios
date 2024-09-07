from pydantic import BaseModel

class Producto(BaseModel):
    codigo: str
    nombre: str
    precio: float
    categoria: str
    stock: int
