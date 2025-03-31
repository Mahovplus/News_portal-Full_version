import os
from fastapi import FastAPI
from app.error_handlers import exception_handlers
from fastapi.staticfiles import StaticFiles
from main_blog.app.mainconf.routes import api_router

static_dir = os.path.normpath('C:\\Python_Projects\\News_portal\\main_blog\\static')
media_dir = os.path.normpath('C:\\Python_Projects\\News_portal\\main_blog\\media')

def create_app():
    app = FastAPI(exception_handlers=exception_handlers)
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.mount('/media', StaticFiles(directory='media'), name='media')
    app.include_router(api_router)
    return app
