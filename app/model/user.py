# form lzx
from app import db
#配置


class User(db.Model):
    """定义数据表

    :数据表中id列: id
    :数据表中name列: name
    :数据表中password列: password
    """
    __tablename__ = 'user'
    #配置数据表的表元素
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64), unique=True)