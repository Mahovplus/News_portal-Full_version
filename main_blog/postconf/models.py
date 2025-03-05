from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from  datetime import datetime, timezone

from sqlalchemy_utils import UUIDType

from main_blog.database import Base


class Post(Base):
    __tablename__ = "post"

    uid = Column(UUIDType, primary_key=True)
    date_create = Column(DateTime, default=datetime.now(timezone.utc))
    is_active = Column(Boolean, default=True)
    title = Column(String)
    content = Column(String)
    owner_id = Column(Integer, ForeignKey("users.uid"))
    owner = relationship("User", back_populates="post")