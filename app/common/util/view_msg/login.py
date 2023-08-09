# from lzx
from app.common.result_code import ResultCode


class LoginMsg:
    """登录页面提示信息

    """
    LOGIN_EMPTY_EXCEPTION = ResultCode(10006, "用户名或者密码为空")

    LOGIN_BUTONG_PASSWORD = ResultCode(10009, "两次密码输入不一致")

    LOGIN_ERROR = ResultCode(10013, "登录失败")

    LOGIN_MSG = ResultCode(200, "请输入用户名和密码")

    LOGIN_USER_NOT_FOUND = ResultCode(10001, "没有找到此用户")

    LOGIN_USERNAME_PASSWORD_EXCEPTION = ResultCode(10008, "用户名或者密码错误")