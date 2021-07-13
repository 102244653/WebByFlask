
from flask import Flask, redirect, request, session, Response, jsonify
from flask_login import LoginManager
from flask_mail import Mail
from myapp.models.base import db

# 初始化 Loginmanager
login_manager = LoginManager()
mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config.from_object('myapp.secure')
    app.config.from_object('myapp.setting')
    # 注册flask-login
    login_manager.init_app(app)
    # 登录页面
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先进行登陆'
    # 邮件注册
    mail.init_app(app)
    # 注册蓝图
    register_blueprint(app)
    # 注册SQLAlchemy
    db.init_app(app)
    db.create_all(app=app)
    app.response_class = AutoJsonifyResponse
    return app


def register_blueprint(app):
    # 注册book里web的蓝图
    from myapp.controller import api
    app.register_blueprint(api)


class AutoJsonifyResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, (list, dict)):
            response = jsonify(response)
        return super(Response, cls).force_type(response, environ)

