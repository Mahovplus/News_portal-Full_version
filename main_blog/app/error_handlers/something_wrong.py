from fastapi import HTTPException, Request

from core.config import TemplateResponse


async def server_error(request: Request, exc: HTTPException):
    return TemplateResponse('C:\\Python_Projects\\News_portal\\main_blog\\templates\\error_pages\\page_500.jinja2',
                            {'request': request})
