from myapp import create_app
from flask import redirect, request, session

app = create_app()


# 请求拦截器，对未登录的链接进行拦截，防止非法访问
# 需要拦截的请求 ： 若用户未登录则跳转到后台登录页面 ， 即 login 路由 。
# 不需要拦截的请求：执行 return None ，即直接跳转到对应请求的路由 。
# 判断用户是否登录：这里我们涉及到 session 的操作 ，若 session 中存在用户名则用户已经登录 ， 反之用户未登录 ，未登录则被拦截的请求直接跳转到 登录路由 login 。
# 添加 session ：session['username'] = 'JeenWang'
# 获取 session ：session.get('username')
# 删除 session ：session.pop('username')
# 清空所有 session ：session.clear()
# @app.before_request
# def before_user():
#     if request.path == "/login":
#         return None
#     if request.path.startswith("/static"):
#         return None
#     if request.path.startswith("/api"):
#         return None
#     if not session.get("username"):
#         return redirect("/login")


if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'], threaded=False)