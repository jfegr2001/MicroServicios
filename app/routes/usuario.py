from fastapi import APIRouter
from fastapi import Body
from ..models.usuario import Usuario


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




