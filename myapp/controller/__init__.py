# 蓝图初始化操作
from flask import Blueprint, render_template

api = Blueprint('controller', __name__)


# @web.app_errorhandler(404)
# def not_found(e):
#     return render_template('404.html')


from . import user

