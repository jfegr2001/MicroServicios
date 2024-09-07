from fastapi import APIRouter, Body
from ..models.producto import Producto

productos_route = APIRouter()

@productos_route.get("/")
async def get_producto():
    try:
        return {"message": "Product data"}
    except Exception as e:
        return {"error": str(e)}

@productos_route.post("/")
async def post_producto(producto: Producto = Body(...)):
    try:
        return {"message": "Product created"}
    except Exception as e:
        return {"error": str(e)}
