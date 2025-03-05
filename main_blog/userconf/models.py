from datetime import datetime, timezone

from sqlalchemy import Column, Boolean, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType, UUIDType

from main_blog.database import Base

utc_now = datetime.now(timezone.utc)

class Users(Base):
    __tablename__= 'users'

    uid = Column(UUIDType, primary_key=True)
    date_create = Column(DateTime, default=utc_now)
    email = Column(EmailType)
    username = Column(String, unique=True)
    hash_password = Column(String)
    is_activ = Column(Boolean, default=True)

    post = relationship('Post', back_populates="owner")