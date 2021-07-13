import base64
import hmac
import time

import itsdangerous
from flask import current_app
from flask_login import UserMixin
from myapp import login_manager
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash

from myapp.models.base import Base, db


class User(Base, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(24), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column('password', String(256))
    image = Column(String(50), nullable=True)
    status = Column(Integer, default=0)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @property
    def info(self):
        return {'id': self.id, 'nickname': self.nickname, 'email': self.email,
                'phone': self.phone_number, 'image': self.image, 'status': self.status, 'token': None}

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    def generate_token(self):
        # 安全码
        salt = current_app.config['SECRET_KEY']
        expiration = current_app.config['EXPIRATION']
        t = itsdangerous.TimedJSONWebSignatureSerializer(salt, expires_in=expiration)  # 过期时间600秒
        info = {'uid': self.id, 'status': self.status}
        token = t.dumps(info).decode('utf-8')
        return token

    def verify_token(self, token):
        salt = current_app.config['SECRET_KEY']
        expiration = current_app.config['EXPIRATION']
        t = itsdangerous.TimedJSONWebSignatureSerializer(salt, expires_in=expiration)  # 过期时间600秒
        try:
            user_detail = t.loads(token.encode('utf-8'))
        except Exception as e:
            return None
        if user_detail.get('status') != -1:
            return User.query.filter_by(id=user_detail.get('uid')).first()
        return None

    @staticmethod
    def reset_password(token, new_password):
        salt = current_app.config['SECRET_KEY']
        expiration = current_app.config['EXPIRATION']
        t = itsdangerous.TimedJSONWebSignatureSerializer(salt, expires_in=expiration)  # 过期时间600秒
        try:
            data = t.loads(token.encode('utf-8'))
        except Exception as e:
            return False
        uid = data.get('uid')
        with db.auto_commit():
            user = User.query.get(uid)
            user.password = new_password
            db.session.add(user)
        return True


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))

