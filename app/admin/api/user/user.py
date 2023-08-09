# form lzx
import requests as requests
from flask import render_template, redirect, url_for, request
from app.form.user_form import ViewForm
from app import app
from app import db
from app.admin.service.user import user
from app.common.util.constants import HTTP_GET, HTTP_POST
from app.common.util.view_msg.user import AddMsg, EditMsg, IndexMsg
import requests



@app.route('/', methods=[HTTP_GET, HTTP_POST])
def index():
    """主api

    :表单对象: register_from
    :数据表所有数据: users
    :return: 主页面的html文件
    """
    index_view = request.args.get('index_view', "请进行操作")
    for t in db.metadata.sorted_tables:
        if "user" == t.name:

            user.creat_db()

    #创建表单对象
    register_form = ViewForm()
    #调用查找数据表中所有元素的处理函数并接收返回值
    users = user.search_all()
    return render_template('user/index.html', data_form=register_form, users=users, tips=index_view)



@app.route('/add', methods=[HTTP_GET, HTTP_POST])
def add_user():
    """添加用户api

    :表单对象: register_from
    :显示页面错误信息变量：view_values
    :页面表单获取的用户名: username
    :页面表单获取的密码和二次输入密码: password,password2
    :return: 返回添加用户的html文件，添加成功后返回主页面的html文件
    """
    # 创建表单对象
    user_add_form = ViewForm()
    view_error = AddMsg.USER_ADD_MSG

    # 获取回送数据
    if request.method == HTTP_POST:
        try:
            username = user_add_form.username.data
            password = user_add_form.password.data
            password2 = user_add_form.password2.data

            if not all([username, password2, password]):
                # 给变量view_error赋错误类型值
                view_error = AddMsg.USER_ADD_EMPTY_EXCEPTION

            elif password != password2:
                # 给变量view_error赋错误类型值
                view_error = AddMsg.USER_ADD_BUTONG_PASSWORD

            else:
                #调用添加业务处理函数
                result, view_error = user.add_user(username, password)
                if result == 1:
                    return redirect(url_for('index'))

        except:
            view_error = AddMsg.USER_ADD_ERROR

    return render_template('user/add.html', data_form=user_add_form, view_tips=view_error)




@app.route('/delete_book/<int:user_id>')
def delete(user_id):
    """删除用户api

    :用户id查找结果: find_user
    :显示主页面信息变量：index_view
    :param user_id: 接收到网页返回的要删除用户的id值
    :return: 主页面的html文件
    """
    index_view = IndexMsg.USER_DELETE_MSG
    #调用查找用户的处理函数并接收查找到的返回值
    find_user = user.search_user(user_id)

    if find_user:

        try:
            #调用删除业务处理函数
            user.delete_serve(find_user)
        except:
            # 给变量index_view赋值
            index_view = IndexMsg.USER_DELETE_ERROR

    else:
        # 给变量index_view赋值
        index_view = IndexMsg.USER_DELETE_NOT_FOUND


    return redirect(url_for('index', index_view=index_view))


@app.route('/edit', methods=[HTTP_GET])
def edit_search():
    """查询需要编辑用户的详细api

    :需要编辑用户id: user_id
    :用户id查找结果: find_user
    :param
    :return: 编辑用户的详细信息，将此传入edit api中
    """

    #获取要编辑的用户id
    user_id = request.args.get('user_id')
    # 调用按用户id查找用户函数接收返回值
    find_user = user.search_user(user_id)
    # 创建编辑用户表单对象
    user_edit_form = ViewForm()

    #定义提示变量值
    view_error = EditMsg.USER_EDIT_MSG

    #return redirect(url_for('edit', find_user=find_user)
    return render_template('user/edit.html', data_form=user_edit_form, view_tips=view_error)



@app.route('/edit', methods=[HTTP_POST])
def edit():
    """查询需要编辑用户的详细api

        :用户id查找结果: find_user
        :表单对象: register_from
        :显示主页面信息变量：index_view
        :页面表单获取的用户名: username
        :页面表单获取的密码和二次输入密码: password,password2
        :param
        :return: 编辑用户的html文件，编辑成功后返回主页面的html文件
        """

    #定义提示变量值
    view_error = EditMsg.USER_EDIT_MSG
    #获取传入的参数
    find_user = request.args.get('find_user')
    if request.method == HTTP_POST:
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        if not all([username, password2, password]):
            # 给变量view_error赋错误类型值
            view_error = EditMsg.USER_EDIT_EMPTY_EXCEPTION
        elif password != password2:
            # 给变量view_error赋错误类型值
            view_error = EditMsg.USER_EDIT_BUTONG_PASSWORD
        else:
            #调用修改用户的处理函数并接收返回值
            result, view_error = user.edit_serve(find_user, username, password)

            if result == 1:
                return redirect(url_for('index'))

    # 创建编辑用户表单对象
    user_edit_form = ViewForm()

    #return redirect(url_for('edit_search', view_tips=view_error))
    return render_template('user/edit.html', data_form=user_edit_form, view_tips=view_error)


