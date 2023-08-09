# form lzx
from app.model.user import User
from app.common.util.view_msg.login import LoginMsg


def land_user(username, password):
    """用户登录的处理函数

    :数据库查找用户名结果: result_name
    :数据库查找密码结果: result_pwd
    :数据库查找用户名和密码的并交结果: result_all
    :param username:在网页端获取到的用户名
    :param password:在网页端获取到的用户密码
    :return:登录成功返回1，失败返回0
    """
    view_error = LoginMsg.LOGIN_MSG.error

    result_name = User.query.filter(User.name == username).first()
    result_pwd = User.query.filter(User.password == password).first()
    result_all = User.query.filter(User.name == username, User.password == password).first()
    print(result_name)

    if result_name is None:
        # 给变量view_error赋错误类型值
        view_error = LoginMsg.LOGIN_USER_NOT_FOUND
        return 0, view_error
    elif result_pwd is None or result_all is None:
        # 给变量view_error赋错误类型值
        view_error = LoginMsg.LOGIN_USERNAME_PASSWORD_EXCEPTION
        return 0, view_error
    else:
        return 1, view_error
