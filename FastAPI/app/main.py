from fastapi import FastAPI
from starlette.responses import RedirectResponse

# Importar los Routers
from routes.usuario_route import users_route
from routes.libro_route import libros_route
from routes.vehiculo_route import vehiculos_route
from routes.evento_route import eventos_route
from routes.producto_route import productos_route


# Base de datos
from database import database as connection
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Conectar a la base de datos si la conexión está cerrada
    if connection.is_closed():
        connection.connect()
    try:
        yield  # Aquí es donde se ejecutará la aplicación
    finally:
        # Cerrar la conexión cuando la aplicación se detenga
        if not connection.is_closed():
            connection.close()


app = FastAPI(lifespan=lifespan)


# Evento de inicio del servidor
@app.on_event("startup")
async def startup_event():
    print("El servidor ha iniciado")

# Evento de cierre del servidor
@app.on_event("shutdown")
async def shutdown_event():
    print("El servidor se ha detenido")



# Ruta para redirigir a la documentación
@app.get("/")
async def docs():
    return RedirectResponse(url="/docs")

# Incluir las rutas de los diferentes módulos
app.include_router(users_route, prefix="/api/users", tags=["Usuarios"])
app.include_router(libros_route, prefix="/api/libros", tags=["Libros"])
app.include_router(vehiculos_route, prefix="/api/vehiculos", tags=["Vehiculos"])
app.include_router(eventos_route, prefix="/api/eventos", tags=["Eventos"])
app.include_router(productos_route, prefix="/api/productos", tags=["Productos"])
