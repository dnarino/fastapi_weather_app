import os
from dotenv import load_dotenv
from typing import Optional
import httpx

load_dotenv()

def get_report(city: str, state: Optional[str], country: str, units: str) -> dict:
    if state:
        q = f"{city},{state},{country}"
    else:
        q = f"{city},{country}"
        
    key = os.getenv("WEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={q}&appid={key}&units={units}"
    
    # Execute the API request
    response = httpx.get(url)
    
    # Fail-fast check
    response.raise_for_status()
    
    return response.json()