from fastapi import APIRouter,Body
from models.usuario import Usuario

from database import UsuarioModel

users_route = APIRouter()

@users_route.get("/")
async def get_user():
    try:
        return{"message": "User date"}
    except Exception as e :
        return {"error" : str(e)}

@users_route.post("/")
async def post_user(usuario : Usuario = Body(...)):

    try:
        return {"message":"User created"}

    except Exception as e:
        return{"error":str(e)}




