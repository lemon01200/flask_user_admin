# form lzx
from app import db
from app.model.user import User
from app.common.util.view_msg.user import AddMsg, EditMsg


def add_user(username, password):
    """添加用户的处理函数

    :在数据库中查询该用户名结果：result_name
    :创建的用户对象: user1
    :显示页面错误信息变量：view_values
    :param username: 网页中获取的用户名
    :return: 添加用户成功返回1，失败返回0
    """
    #查找该用户名在数据库中是否存在
    result_name = User.query.filter(User.name == username).first()
    #在用户未存在时，在数据库中添加该用户
    if result_name is None:
        user1 = User(name=username, password=password)

        db.session.add(user1)
        db.session.commit()

        #给变量view_error赋提示值
        view_mesg = AddMsg.USER_ADD_MSG
        return 1, view_mesg
    else:
        #变量view_error赋错误类型值
        view_error = AddMsg.USER_ADD_EXIST
        return 0, view_error



def creat_db():
    """创建数据库的处理函数

    :return: 无返回值
    """
    db.create_all()



def edit_serve(user, username, password):
    """修改用户的处理函数

    :数据库查找用户名结果: result_name
    :数据库查找密码结果: result_pwd
    :显示页面错误信息变量：view_values
    :param user: 要进行修改的用户对象
    :param username: 从网页中获取的用户名
    :param password: 从网页中获取的密码
    :return: 修改成功返回1，失败返回0
    """

    #在数据库中查找用户名和密码
    result_name = User.query.filter(User.name == username).first()
    result_pwd = User.query.filter(User.password == password).first()
    if (result_name is None and result_pwd is None) or (user.name == username or user.password == password):

        if user.name == username and user.password == password:
            # 给变量view_error赋错误类型值
            view_error = EditMsg.USER_EDIT_XIAONGTONG
            return 0, view_error
        else:
            user.name = username
            user.password = password

            db.session.commit()

            # 给变量view_error赋提示值
            view_mesg = EditMsg.USER_EDIT_MSG
            return 1, view_mesg
    else:
        # 给变量error_values赋错误类型值
        view_error = EditMsg.USER_EDIT_EXIST
        return 0, view_error



def delete_serve(user):
    """删除用户的处理函数

    :param user: 要进行删除的用户对象
    :return:无返回值
    """
    db.session.delete(user)
    db.session.commit()



def search_user(user_id):
    """用用户id查找用户的处理函数

    :数据库查找用户id结果: user
    :param user_id: 要查找用户的用户id
    :return: 在数据库内查找到的值
    """
    user = User.query.get(user_id)
    return user



def search_all():
    """查找数据表中所有元素的处理函数

    :数据库内的所有数据: user_all
    :return: 返回在数据库内查找到的值
    """
    user_all = User.query.all()
    return user_all
