from fastapi import HTTPException, Request, FastAPI
from core.config import TemplateResponse

app = FastAPI()

@app.exception_handler(HTTPException)
async def server_error(request: Request, exc: HTTPException):
    return TemplateResponse('error_pages\\page_500.jinja2',
                            {'request': request})
