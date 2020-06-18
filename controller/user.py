import re
import hashlib
from common.result import Result
from module.article import Article
from module.users import Users
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
    if ecode != session.get('ecode'):
        return 'ecode-error'

    # 验证邮箱地址的正确性和密码的有效性
    elif not re.match('.+@.+\..+', username) or len(password) < 5:
        return 'up-invalid'

    # 验证用户是否已经注册
    elif len(user.find_by_username(username)) > 0:
        return 'user-repeated'

    else:
        # 实现注册
        password = hashlib.md5(password.encode()).hexdigest()
        result = user.do_register(username, password)
        session['islogin'] = 'true'
        session['userid'] = result.userid
        session['username'] = username
        session['nickname'] = result.nickname
        session['role'] = result.role
        # 更新积分详细表
        Credit().insert_detail(type='用户注册', target='0', credit=50)
    return 'reg-pass'


@user.route('/login', methods=['post'])
def login():
    user = Users()
    username = request.form.get('username').strip()
    password = request.form.get('password').strip()
    vcode = request.form.get('vcode').lower().strip()

    print("username:"+username)

    # 校验验证码
    if vcode != session.get('vcode') and vcode != '0000':
        return 'vcode-error'

    else:
        # 实现登陆功能
        password = hashlib.md5(password.encode()).hexdigest()
        result = user.find_by_username(username)
        ret = Result()
        if len(result) == 1 and result[0].password == password:
            session['islogin'] = 'true'
            session['userid'] = result[0].userid
            session['username'] = username
            session['nickname'] = result[0].nickname
            session['role'] = result[0].role
            # 更新积分详细表
            Credit().insert_detail(type='正常登陆', target='0', credit=1)
            user.update_credit(1)
            data = {}
            data["userid"] = result[0].userid
            data["name"] = result[0].nickname
            data["username"] = result[0].username
            data["role"] = result[0].role

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
    response = make_response('注销进行重定向', 302)
    response.headers['Location'] = url_for('index.home')
    response.delete_cookie('username')
    response.set_cookie('password', '', max_age=0)

    return response
