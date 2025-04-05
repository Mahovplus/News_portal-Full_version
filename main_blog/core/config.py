import os
from pathlib import Path
from core.img_extension import IMG_EXTENSION_LIST
from fastapi.templating import Jinja2Templates
from pydantic import BaseSettings
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

SECRET_KEY = b"SECRET_KEY"
if not SECRET_KEY:
    SECRET_KEY = os.urandom(32)

SQLALCHEMY_DATABASE_URL = 'sqlite:///./site.db'
#ALEMBIC_SQLALCHEMY_DATABASE_URL = 'sqlite:///./site.db'

ROOT_URL = Path(__file__).resolve().parent.parent
MEDIA_URL = os.path.join(ROOT_URL, 'media')

#templates_dir = os.path.normpath('C:\\Python_Projects\\News_portal\\main_blog\\templates')
templates = Jinja2Templates(directory='main_blog/templates')
TemplateResponse = templates.TemplateResponse

mail_conf = ConnectionConfig(
    MAIL_USERNAME="mahovplus666@mail.ru",
    MAIL_PASSWORD="vvR38X0Ccrs3r6Vhiq0k",
    MAIL_FROM="mahovplus666@mail.ru",
    MAIL_PORT=465,
    MAIL_SERVER="smtp.mail.ru",
    MAIL_FROM_NAME="Test Messages",
    MAIL_TLS=False,
    MAIL_SSL=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)
