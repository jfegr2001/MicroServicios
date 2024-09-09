from fastapi import APIRouter, Body
from models.libro import Libro

libros_route = APIRouter()

@libros_route.get("/")
async def get_libro():
    try:
        return {"message": "Book data"}
    except Exception as e:
        return {"error": str(e)}

@libros_route.post("/")
async def post_libro(libro: Libro = Body(...)):
    try:
        return {"message": "Book created"}
    except Exception as e:
        return {"error": str(e)}
