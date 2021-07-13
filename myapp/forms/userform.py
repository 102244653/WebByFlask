from wtforms import Form, StringField, PasswordField
from wtforms.form import BaseForm
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo

from myapp.forms.jsonform import JsonForm
from myapp.models.user import User


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规则')])
    password = PasswordField(validators=[DataRequired('密码不能为空，请输入密码'), Length(6, 32)])
    nickname = StringField(validators=[DataRequired(), Length(2, 10, message='昵称最少需要两个字符，最多10个字符')])
    phone_number = StringField(validators=[DataRequired(), Length(11, message='手机号格式不对')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮箱已经被注册')

    def validate_phone(self, field):
        if User.query.filter_by(phone_number=field.data).first():
            raise ValidationError('手机号已经被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已经被注册')


class LoginForm(JsonForm):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规则')])
    password = PasswordField(validators=[DataRequired('密码不能为空，请输入密码'), Length(6, 32)])


class ResetPasswordForm(JsonForm):
    password1 = PasswordField(validators=[DataRequired('密码不能为空，请输入密码'), Length(6, 32, message='密码长度需要在6到32位之间'), EqualTo('password2', message='两次输入的密码不一致')])
    password2 = PasswordField(validators=[DataRequired('确认密码不能为空，请输入密码')])
    token = StringField(validators=[DataRequired('token不能为空')])
