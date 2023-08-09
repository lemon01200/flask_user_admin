# from lzx
from app.common.result_code import ResultCode


class EditMsg:
    """编辑操作的提示信息

    """
    USER_EDIT_XIAONGTONG = ResultCode(10002, "用户名和密码与之前相同")

    USER_EDIT_MSG = ResultCode(200, "请输入用户名和密码")

    USER_EDIT_EXIST = ResultCode(10003, "用户已经存在")

    USER_EDIT_EMPTY_EXCEPTION = ResultCode(10006, "用户名或者密码为空")

    USER_EDIT_BUTONG_PASSWORD = ResultCode(10009, "两次密码输入不一致")


class AddMsg:
    """添加操作的提示信息

    """
    USER_ADD_MSG = ResultCode(200, "请输入用户名和密码")

    USER_ADD_EMPTY_EXCEPTION = ResultCode(10006, "用户名或者密码为空")

    USER_ADD_BUTONG_PASSWORD = ResultCode(10009, "两次密码输入不一致")

    USER_ADD_ERROR = ResultCode(10010, "用户添加失败")

    USER_ADD_EXIST = ResultCode(10003, "用户已经存在")


class IndexMsg:
    """主页面的提示信息

    """
    USER_DELETE_ERROR = ResultCode(10004, "删除用户失败")

    USER_DELETE_NOT_FOUND = ResultCode(10001, "没有找到此用户")

    USER_DELETE_MSG = ResultCode(200, "请进行操作")