import fastapi

router =fastapi.APIRouter()

@router.get('/api/weather')
def weather():
    return "Here will go the weather page.."