from typing import Optional
import fastapi
from fastapi import Depends
from pydantic import BaseModel
import httpx

#models
from models.location import Location

#services
from services import openweather_service

router =fastapi.APIRouter()


@router.get('/api/weather/{city}')
def weather(location:Location = Depends(), units:Optional[str] ='metric'):
    try:
        report = openweather_service.get_report(location.city, location.state, location.country, units)
        return report
    except httpx.HTTPStatusError as exc:
        # Fail-fast: return the exact error from OpenWeatherMap to the client
        return fastapi.responses.JSONResponse(
            status_code=exc.response.status_code,
            content=exc.response.json()
        )
    except Exception as exc:
        raise fastapi.HTTPException(status_code=500, detail=str(exc))