import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from main_blog.app.mainconf.routes import api_router

static_dir = os.path.normpath('C:\\Python_Projects\\News_portal\\main_blog\\static')
media_dir = os.path.normpath('C:\\Python_Projects\\News_portal\\main_blog\\media')

def create_app(debug=True):
    app = FastAPI(debug=debug)
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.mount('/media', StaticFiles(directory='media'), name='media')
    app.include_router(api_router)
    return app
