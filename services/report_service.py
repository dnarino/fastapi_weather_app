import uuid
from datetime import datetime
from models.reports import Report
from models.location import Location
from typing import List

__reports: List[Report] = [
    Report(
        id=str(uuid.uuid4()),
        location=Location(city="Bogotá", state="Cundinamarca", country="COL"),
        description="Heavy rain and thunderstorms in the afternoon.",
        created_time=datetime.now()
    ),
    Report(
        id=str(uuid.uuid4()),
        location=Location(city="Medellín", state="Antioquia", country="COL"),
        description="Warm and sunny morning with light breeze.",
        created_time=datetime.now()
    )
]

async def get_reports() -> List[Report]:
    return list(__reports)

async def add_report(description:str, location:Location) -> Report:
    now = datetime.now()
    report = Report(
        id=str(uuid.uuid4()),
        location=location,
        description=description,
        created_time=now)
    
    __reports.insert(0, report)

    return report