
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, current_user, logout_user, login_required
from myapp.forms.userform import RegisterForm, LoginForm, ResetPasswordForm
from myapp.models.base import db
from . import api
from ..models.result import Result
from ..models.user import User


@api.route('/index')
@login_required
def index():
    return "hello,word!"


@api.route('/user/register', methods=['POST'])
def register():
    wt_form = RegisterForm(request.form)
    if wt_form.validate():
        with db.auto_commit():
            user = User()
            # 赋值已校验过的值
            user.set_attr(wt_form.data)
            db.session.add(user)
        return Result.success("注册成功",  wt_form.email.data)
    # 返回所有错误信息
    return Result.fail("注册失败", wt_form.errors)


@api.route('/user/login', methods=['POST'])
def login():
    wt_form = LoginForm().init_and_validate()
    if wt_form.validate():
        user = User.query.filter_by(email=wt_form.email.data).first()
        if user and user.check_password(wt_form.password.data):
            login_user(user)
            detail = user.info
            detail['token'] = user.generate_token()
            return Result.success("登录成功", detail)
        else:
            return Result.fail("登录失败", '账号不存在或密码错误')
    return Result.fail("登录失败", wt_form.errors)


@api.route('/user/reset/password', methods=["POST"])
# @login_required
def reset_password():
    # 判断是登录的
    if not current_user.is_authenticated:
        return Result.fail("账号未登录")
    pw_form = ResetPasswordForm().init_and_validate()
    if pw_form.validate():
        if User.reset_password(pw_form.token.data, pw_form.password1.data):
            return Result.success("密码修改成功")
    return Result.fail("密码修改失败", pw_form.errors)


@api.route('/user/logout')
@login_required
def logout():
    # 判断是登录的
    if not current_user.is_authenticated:
        return Result.fail("账号未登录")
        logout_user()
    return Result.success("退出成功")