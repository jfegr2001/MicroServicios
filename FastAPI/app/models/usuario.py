from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    name: str
    email: str
    address: str
    age: int




