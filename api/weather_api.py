# Group 1: Standard Libraries
from typing import Optional

# Group 2: Third-Party Libraries
import fastapi
from fastapi import Depends
import httpx

# Group 3: Local/Internal Imports
from models.location import Location
from services import openweather_service

router = fastapi.APIRouter()



@router.get('/api/weather/{city}')
async def weather(location:Location = Depends(), units:Optional[str] ='metric'):
    report = await openweather_service.get_report_async(location.city, location.state, location.country, units)
    return report