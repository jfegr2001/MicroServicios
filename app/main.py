from fastapi import FastAPI
from starlette.responses import RedirectResponse

# Importar los Routers
from app.routes.usuario import users_route
from app.routes.libro import libros_route
from app.routes.vehiculo import vehiculos_route
from app.routes.evento import eventos_route
from app.routes.producto import productos_route

# Crear una instancia de FastAPI
app = FastAPI()

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
app.include_router(users_route, prefix="/users", tags=["Usuarios"])
app.include_router(libros_route, prefix="/libros", tags=["Libros"])
app.include_router(vehiculos_route, prefix="/vehiculos", tags=["Vehiculos"])
app.include_router(eventos_route, prefix="/eventos", tags=["Eventos"])
app.include_router(productos_route, prefix="/productos", tags=["Productos"])
