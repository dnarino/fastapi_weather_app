import fastapi
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = fastapi.APIRouter()


@router.get('/')
def index(request: fastapi.Request):
    return templates.TemplateResponse(
        request=request,
        name="home/index.html",
        context={}
    )

@router.get('/favicon.ico')
def favicon():
    return fastapi.responses.RedirectResponse(url='/static/img/favicon.ico')