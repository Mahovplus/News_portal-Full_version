from typing import Optional
from pydantic import BaseModel
import datetime
from main_blog.app.userconf.schemas import User


class PostBase(BaseModel):
    title: str
    body: str


class PostList(PostBase):
    created_date: Optional[datetime.datetime]
    owner_id: int
    owner: User

    class Config:
        orm_mode = True

