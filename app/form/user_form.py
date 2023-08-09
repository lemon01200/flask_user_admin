# from lzx

#导入wtf表单
from flask_wtf import FlaskForm
#导入自定义表单使用的表单功能
from wtforms import SubmitField, StringField, PasswordField


class ViewForm(FlaskForm):
    """html中显示的表单类

    """
    username = StringField(label="用户名")
    password = PasswordField('密码')
    password2 = PasswordField('确认密码')
    input = SubmitField('提交')