import re
import hashlib
from common.result import Result
from module.article import Article
from module.user import Users
from module.credit import Credit
from flask import Blueprint, make_response, session, request, redirect, url_for


user = Blueprint('user', __name__)


@user.route('/user', methods=['post'])
def register():
    user = Users()
    username = request.form.get('username').strip()
    password = request.form.get('password').strip()
    ecode = request.form.get('ecode').strip()

    # 校验邮箱验证码
    if ecode != session.get('ecode') and ecode != '0000':
        ret = Result()
        return ret.fail(402, 'ecode-error', '')

    # # 验证邮箱地址的正确性和密码的有效性
    # elif not re.match('.+@.+\..+', username) or len(password) < 5:
    #     return 'up-invalid'

    # 验证用户是否已经注册
    elif len(user.find_by_username(username)) > 0:
        ret = Result()
        return ret.fail(403, 'user-repeated', username)

    else:
        # 实现注册
        password = hashlib.md5(password.encode()).hexdigest()
        result = user.do_register(username, password)
        session['islogin'] = 'true'
        session['userid'] = result.userid
        session['username'] = username
        session['nickname'] = result.nickname
        session['role'] = result.role
        ret = result()
    return ret.succ('reg-pass')


@user.route('/login', methods=['post'])
def login():
    user = Users()
    username = request.form.get('username').strip()
    password = request.form.get('password').strip()
    vcode = request.form.get('vcode').lower().strip()

    print("username:" + username)

    # 校验验证码
    if vcode != session.get('vcode') and vcode != '0000':
        ret = Result()
        return ret.fail(402, 'vcode-error', '')

    else:
        # 实现登陆功能
        password = hashlib.md5(password.encode()).hexdigest()
        result = user.find_by_username(username)
        ret = Result()
        if len(result) == 1 and result[0].password == password:
            session['islogin'] = 'true'
            session['userid'] = result[0].id
            session['username'] = username
            session['nickname'] = result[0].name
            data = {}
            data["userid"] = result[0].id
            data["name"] = result[0].name
            data["username"] = result[0].username

            # 将Cookie写入浏览器
            response = make_response(ret.succ(data))
            response.set_cookie('username', username, max_age=30*24*3600)
            response.set_cookie('password', password, max_age=30*24*3600)

            return response
        else:

            return ret.fail(401, 'login-fail', "")


@user.route('/logout')
def logout():
    # 清空session， 页面跳转
    session.clear()
    response = make_response(Result().succ('登出成功'), 302)
    # response.headers['Location'] = url_for('index.home')
    response.delete_cookie('username')
    response.set_cookie('password', '', max_age=0)

    return response
