from pydantic import BaseModel

class Libro(BaseModel):
    isbn: str
    titulo: str
    autor: str
    editorial: str
    paginas: int
