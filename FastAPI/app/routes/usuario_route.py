from fastapi import APIRouter, Body
from models.usuario import Usuario
from database import UsuarioModel

usuario_route = APIRouter()

@usuario_route.get("/usuarios")
def get_usuarios():
    return list(UsuarioModel.select())

@usuario_route.get("/usuarios/{user_id}")
def get_usuario(user_id: int):
    return UsuarioModel.get(UsuarioModel.id == user_id)

@usuario_route.post("/usuarios")
def create_usuario(usuario: Usuario = Body(...)):
    nuevo_usuario = UsuarioModel.create(
        name=usuario.name,
        email=usuario.email,
        address=usuario.address,
        age=usuario.age
    )
    return nuevo_usuario

@usuario_route.put("/usuarios/{user_id}")
def update_usuario(user_id: int, usuario_data: dict):
    UsuarioModel.update(**usuario_data).where(UsuarioModel.id == user_id).execute()
    return {"message": "Usuario actualizado"}

@usuario_route.delete("/usuarios/{user_id}")
def delete_usuario(user_id: int):
    UsuarioModel.delete().where(UsuarioModel.id == user_id).execute()
    return {"message": "Usuario eliminado"}


