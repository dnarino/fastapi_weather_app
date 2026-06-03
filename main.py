import fastapi
import uvicorn
from fastapi.staticfiles import StaticFiles

#imports
from api import weather_api
from views import home


api = fastapi.FastAPI()

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