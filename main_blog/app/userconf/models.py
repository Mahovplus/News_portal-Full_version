from datetime import datetime, timezone

from uuid import uuid4

from sqlalchemy import Column, Boolean, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType, UUIDType


from app.postconf.models import Post
from db.base_class import Base

from authlib.jose import JsonWebSignature
import json
import time
from core.config import SECRET_KEY

utc_now = datetime.now(timezone.utc)

class User(Base):
    """ Наименование колон и полей """

    __table_args__ = {'extend_existing': True}

    uid = Column(UUIDType, default=uuid4, primary_key=True)
    created_date = Column(DateTime, default=utc_now)
    email = Column(EmailType)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    posts = relationship("Post", back_populates="owner")
    token = Column(String(64), nullable=True)

    def __repr__(self):
        return f"<User(uid={self.uid}, username={self.username}, email={self.email})>"

    def get_reset_token(self, expires_sec=1800):
        jws = JsonWebSignature(['HS256'])
        protected = {'alg': 'HS256'}
        payload = json.dumps({'expires_sec': expires_sec,
                              'time_sending': time.time(),
                              'user_uid': str(self.uid)}).encode('utf-8')
        secret = SECRET_KEY
        return jws.serialize_compact(protected, payload, secret).decode('utf-8')

    @staticmethod
    def get_payload_from_reset_token(token):
        jws = JsonWebSignature(['HS256'])
        data = jws.deserialize_compact(token, SECRET_KEY)
        payload_json = json.loads(data['payload'])

        time_left = payload_json['time_sending'] + payload_json['expires_sec'] - time.time()
        print(time_left)
        if time_left < 0:
            return False
        else:
            return payload_json


class Token(Base):
    """ table args"""
    __table_args__ = {'extend_existing': True}

    uid = Column(UUIDType, default=uuid4, primary_key=True)
    token = Column(UUIDType, unique=True, nullable=False, index=True, default=uuid4)
    expires = Column(DateTime())
    user_uid = Column(UUIDType, ForeignKey('user.uid'))