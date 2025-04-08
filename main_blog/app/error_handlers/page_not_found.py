from fastapi import HTTPException, Request, FastAPI
from core.config import TemplateResponse

app = FastAPI()

@app.exception_handler(HTTPException)
async def not_found(request: Request, exc: HTTPException):
    return TemplateResponse('error_pages/page_not_found.jinja2',
                            {'request': request})