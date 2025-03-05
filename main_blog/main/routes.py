from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os

static_dir = os.path.normpath('C:\\Python_Projects\\News_portal\\main_blog\\templates')

templates = Jinja2Templates(directory=static_dir)
router = APIRouter()

@router.get('/', response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})