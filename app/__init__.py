# form lzx
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configparser import ConfigParser
import pymysql
from configs import Config

# 创建app对象
# 更改flask查找模板文件目录
app = Flask(__name__, template_folder='templates/admin')
# 加载配置文件，db创建前需要对数据库进行配置
# 加载配置文件
app.config.from_pyfile('D://flaskProject//flaskdemo//db.ini')
#app.config.from_object(Config)

# 创建db对象
pymysql.install_as_MySQLdb()
db = SQLAlchemy(app)
# db绑定app
db.init_app(app)

#导入蓝图所在的文件
from app.login.api.login.login import login_bl
# 将蓝图注册到app
app.register_blueprint(login_bl, url_prefix='/app/login/api/login/login')

#导入用户相关的api
from app.admin.api.user import user
