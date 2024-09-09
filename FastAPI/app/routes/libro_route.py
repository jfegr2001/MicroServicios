from fastapi import APIRouter, Body
from models.libro import Libro
from database import LibroModel

libro_route = APIRouter()

@libro_route.get("/libros")
def get_libros():
    return list(LibroModel.select())

@libro_route.get("/libros/{isbn}")
def get_libro(isbn: str):
    return LibroModel.get(LibroModel.isbn == isbn)

@libro_route.post("/libros")
def create_libro(libro: Libro = Body(...)):
    nuevo_libro = LibroModel.create(
        isbn=libro.isbn,
        titulo=libro.titulo,
        autor=libro.autor,
        editorial=libro.editorial,
        paginas=libro.paginas
    )
    return nuevo_libro

@libro_route.put("/libros/{isbn}")
def update_libro(isbn: str, libro_data: dict):
    LibroModel.update(**libro_data).where(LibroModel.isbn == isbn).execute()
    return {"message": "Libro actualizado"}

@libro_route.delete("/libros/{isbn}")
def delete_libro(isbn: str):
    LibroModel.delete().where(LibroModel.isbn == isbn).execute()
    return {"message": "Libro eliminado"}
