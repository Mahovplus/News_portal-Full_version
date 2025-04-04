from fastapi import HTTPException, Request, FastAPI
from core.config import TemplateResponse

app = FastAPI()

@app.exception_handler(HTTPException)
async def no_access(request: Request, exc: HTTPException):
    return TemplateResponse('error_pages\\page_403.jinja2',
                            {'request': request})
