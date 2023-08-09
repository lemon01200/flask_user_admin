# form lzx
from flask import request, render_template, Blueprint
from app.form.user_form import ViewForm
from app.login.service.login import login
from app.common.util.constants import HTTP_POST, HTTP_GET
from app.common.util.view_msg.login import LoginMsg


#创建一个蓝图
login_bl = Blueprint('login_bl', __name__, root_path="/login")





@login_bl.route('/landing', methods=[HTTP_GET, HTTP_POST])
def landing():
    """用户登录api

    :表单对象: register_form
    :显示页面错误信息变量：view_error
    :页面表单获取的用户名: username
    :页面表单获取的密码和二次输入密码: password,password2
    :REQUEST_MENTION_GET:常量GET
    :REQUEST_MENTION_POST:常量POST
    :return:返回用户登录的html文件
    """
    # 创建表单对象
    login_form = ViewForm()
    view_error = LoginMsg.LOGIN_MSG

    if request.method == 'POST':

        try:
            username = login_form.username.data
            password = login_form.password.data
            password2 = login_form.password2.data
            if not all([username, password2, password]):
                # 给变量view_error赋错误类型值
                view_error = LoginMsg.LOGIN_EMPTY_EXCEPTION

            elif password != password2:
                # 给变量view_error赋错误类型值
                view_error = LoginMsg.LOGIN_BUTONG_PASSWORD
            else:
                result, view_error = login.land_user(username, password)
                print(view_error.error)
                if result == 1:
                    return "登录成功"

        except:
            # 给变量view_error赋错误类型值
            view_error = LoginMsg.LOGIN_ERROR

    return render_template('login/login.html', data_form=login_form, view_tips=view_error)
