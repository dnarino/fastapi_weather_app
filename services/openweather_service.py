import httpx
import os
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

client = httpx.AsyncClient()

async def get_report_async(city: str, state: Optional[str], country: str, units: str) -> dict:
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
    return forecast

async def close_client():
    await client.aclose()