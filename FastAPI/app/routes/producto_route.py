from fastapi import APIRouter, Body
from models.producto import Producto
from database import ProductoModel

producto_route = APIRouter()

@producto_route.get("/productos")
def get_productos():
    return list(ProductoModel.select())

@producto_route.get("/productos/{codigo}")
def get_producto(codigo: str):
    return ProductoModel.get(ProductoModel.codigo == codigo)

@producto_route.post("/productos")
def create_producto(producto: Producto = Body(...)):
    nuevo_producto = ProductoModel.create(
        codigo=producto.codigo,
        nombre=producto.nombre,
        precio=producto.precio,
        categoria=producto.categoria,
        stock=producto.stock
    )
    return nuevo_producto

@producto_route.put("/productos/{codigo}")
def update_producto(codigo: str, producto_data: dict):
    ProductoModel.update(**producto_data).where(ProductoModel.codigo == codigo).execute()
    return {"message": "Producto actualizado"}

@producto_route.delete("/productos/{codigo}")
def delete_producto(codigo: str):
    ProductoModel.delete().where(ProductoModel.codigo == codigo).execute()
    return {"message": "Producto eliminado"}
