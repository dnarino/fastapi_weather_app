import os
import fastapi

from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()
# Retrieve the secret key
API_KEY = os.getenv("WEATHER_API_KEY")

router =fastapi.APIRouter()

@router.get('/api/weather')
def weather():
    return "Here will go the weather page.."