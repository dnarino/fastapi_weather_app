# Group 1: Standard Libraries
from models.reports import ReportSubmittal
from services import report_service
from models.reports import Report
from typing import Optional

# Group 2: Third-Party Libraries
# pyrefly: ignore [missing-import]
import fastapi
from fastapi import Depends

# Group 3: Local/Internal Imports
from models.location import Location
from services import openweather_service

router = fastapi.APIRouter()



@router.get('/api/weather/{city}')
async def weather(location:Location = Depends(), units:Optional[str] ='metric'):
    report = await openweather_service.get_report_async(location.city, location.state, location.country, units)
    return report

@router.get('/api/reports', name='all_reports')
async def get_reports() -> list[Report]:
    return await report_service.get_reports()

@router.post('/api/reports', name='add_report', status_code=201)
async def report_post(report_submittal:ReportSubmittal) -> Report:
    d =report_submittal.description
    loc=report_submittal.location
    return await report_service.add_report(d,loc)

