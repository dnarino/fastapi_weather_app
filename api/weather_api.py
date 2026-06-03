from typing import Optional
import os
import fastapi
from fastapi import Depends
from pydantic import BaseModel

from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()
# Retrieve the secret key
API_KEY = os.getenv("WEATHER_API_KEY")

router =fastapi.APIRouter()

#pydantic Model

class Location(BaseModel):
    city:str
    state:Optional[str]=None
    country:Optional[str] = 'COL'

@router.get('/api/weather/{city}')
def weather(location:Location = Depends(),
            units:Optional[str] ='metric'):
    return f"{location.city}, {location.state}, {location.country} in {units}"