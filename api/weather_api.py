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
    try:
        report = await openweather_service.get_report_async(location.city, location.state, location.country, units)
        return report
    except httpx.HTTPStatusError as exc:
        # Fail-fast: return the exact error from OpenWeatherMap to the client
        return fastapi.responses.JSONResponse(
            status_code=exc.response.status_code,
            content=exc.response.json()
        )
    except Exception as exc:
        raise fastapi.HTTPException(status_code=500, detail=str(exc))