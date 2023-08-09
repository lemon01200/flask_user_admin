# form lzx

class Config(object):
    """db对象的配置文件

    """
    #配置数据库地址
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql123456@127.0.0.1/new_project"
    #关闭警告信息
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #配置表单的key值
    SECRET_KEY = 'LZX'






