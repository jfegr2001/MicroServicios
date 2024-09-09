from dotenv import load_dotenv
from peewee import *

import os

load_dotenv()

database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)

class EventoModel(Model):
    id = AutoField(primary_key=True)
    nombre = CharField(max_length=100)
    fecha = CharField(max_length=50)
    ubicacion = CharField(max_length=100)
    organizador = CharField(max_length=100)
    capacidad = IntegerField()

    class Meta:
        database = database
        table_name = "eventos"


class LibroModel(Model):
    isbn = CharField(primary_key=True, max_length=20)
    titulo = CharField(max_length=100)
    autor = CharField(max_length=100)
    editorial = CharField(max_length=100)
    paginas = IntegerField()

    class Meta:
        database = database
        table_name = "libros"



class ProductoModel(Model):
    codigo = CharField(primary_key=True, max_length=20)
    nombre = CharField(max_length=100)
    precio = FloatField()
    categoria = CharField(max_length=50)
    stock = IntegerField()

    class Meta:
        database = database
        table_name = "productos"


class UsuarioModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    email = CharField(max_length=50)
    address = CharField(max_length=100)
    age = IntegerField()

    class Meta:
        database = database
        table_name = "usuarios"


class VehiculoModel(Model):
    marca = CharField(max_length=50)
    modelo = CharField(max_length=50)
    cilindraje = IntegerField()
    color = CharField(max_length=30)
    matricula = CharField(primary_key=True, max_length=20)

    class Meta:
        database = database
        table_name = "vehiculos"