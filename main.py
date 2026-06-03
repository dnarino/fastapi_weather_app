from contextlib import asynccontextmanager
import fastapi
import uvicorn
from fastapi.staticfiles import StaticFiles

#imports
from api import weather_api
from views import home
from services import openweather_service

@asynccontextmanager
async def lifespan(app:fastapi.FastAPI):
    yield
    await openweather_service.close_client()

api = fastapi.FastAPI(lifespan=lifespan)

def configure():
    configure_routing()

# Register routers
def configure_routing():
    # Mount the static folder so FastAPI can serve the CSS and images
    api.mount("/static", StaticFiles(directory="static"), name="static")
    api.include_router(home.router)
    api.include_router(weather_api.router)



if __name__== '__main__':
    configure()
    uvicorn.run("main:api", port=8000, host='127.0.0.1', reload=True)
else:
    configure()