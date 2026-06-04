from infraestructure import weather_cache
import httpx
import os
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

client = httpx.AsyncClient()

async def get_report_async(city: str, state: Optional[str], country: str, units: str) -> dict:
    
    if forecast:=weather_cache.get_weather(city,state,country,units):
        return forecast
    if state:
        q = f"{city},{state},{country}"
    else:
        q = f"{city},{country}"
        
    key = os.getenv("WEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={q}&appid={key}&units={units}"
    
    
    # Execute the API request
    response = await client.get(url)
    
    # Fail-fast check
    response.raise_for_status()
    
    data =response.json()
    forecast = data['main']
    weather_cache.set_weather(city,state,country,units,forecast)
    return forecast

async def close_client():
    await client.aclose()