from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from main_blog.main.routes import router

from main_blog.database import engine
from main_blog.userconf import models
from main_blog.postconf import models
import os
models.Base.metadata.create_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

static_dir = os.path.normpath('C:\\Python_Projects\\News_portal\\main_blog\\static')

def create_app(debug=True):
    app = FastAPI(debug=debug)
    app.mount('/static', StaticFiles(directory=static_dir), name='static')
    app.include_router(router)
    return app

