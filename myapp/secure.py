DEBUG = True  # 是否开启Debug
HOST = '0.0.0.0'  # 0.0.0.0表示访问权限为全网
PORT = 8081  # 访问端口号

# mysql连接，比如 SQLALCHEMY_DATABASE_URI='mysql+cymysql://root:root@localhost:3306/fisher'
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root1234@127.0.0.1:3306/fisher'

# 回滚
SQLALCHEMY_TRACK_MODIFICATIONS = True
# 自动提交
SQLALCHEMY_COMMIT_TEARDOWN = True
# 打印sql
SQLALCHEMY_ECHO = True

# 设置key
SECRET_KEY = 'vantop'
# token有效时间
EXPIRATION = 600

# Email 配置
# MAIL_SERVER = 'smtp.exmail.qq.com'
# MAIL_PORT = 465
# MAIL_USE_SSL = True
# MAIL_USE_TSL = False
# MAIL_USERNAME = 'admin@guaosi.com'
# MAIL_PASSWORD = '' #密码
# MAIL_SUBJECT_PREFIX = '[鱼书]'
# MAIL_SENDER = '鱼书 <admin@guaosi.com>'
