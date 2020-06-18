import math

from flask import Blueprint, render_template, abort, jsonify, session, request
from module.article import Article
from module.users import Users
from module.credit import Credit
index = Blueprint("index", __name__)
npp = 10


@index.route('/')
def home():
    # if session.get('islogin') is None:
    #     username = request.cookies.get('username')
    #     password = request.cookies.get('password')
    #     user = Users()
    #     if username != None and password != None:
    #         # 实现登陆功能
    #         result = user.find_by_username(username)
    #         if len(result) == 1 and result[0].password == password:
    #             session['islogin'] = 'true'
    #             session['userid'] = result[0].userid
    #             session['username'] = username
    #             session['nickname'] = result[0].nickname
    #             session['role'] = result[0].role

    article = Article()
    result = article.find_limit_with_users(0, npp)
    total = math.ceil(article.get_total_count() / npp)

    last, most, recommended = article.find_last_most_recommended()

    return render_template('index.html', result=result, page=1, total=total,
                           last=last, most=most, recommended=recommended)


@index.route('/page/<int:page>')
def paginate(page):
    start = (page - 1) * npp  # 1==>0, 2==>10
    article = Article()
    result = article.find_limit_with_users(start, npp)
    total = math.ceil(article.get_total_count() / npp)
    return render_template('index.html', result=result, page=page, total=total)


@index.route('/type/<int:type>-<int:page>')
def classify(type, page):
    article = Article()
    start = (page - 1) * npp  # 1==>0, 2==>10
    result = article.find_by_type(type, start, npp)
    total = math.ceil(article.get_count_by_type(type) / npp)
    return render_template('type.html', result=result, page=page, total=total, type=type)


@index.route('/search/<int:page>-<keyword>')
def search(page, keyword):
    keyword = keyword.strip()
    if keyword is None or keyword == '' or '%' in keyword or len(keyword) > 10:
        abort(404)

    start = (page - 1) * npp
    article = Article()
    result = article.find_by_headline(keyword, start, npp)
    total = math.ceil(article.get_count_by_headline(keyword) / npp)

    return render_template('search.html', result=result, page=page, total=total, keyword=keyword)


@index.route('/recommend')
def recommend():
    article = Article()
    last, most, recommended = article.find_last_most_recommended()
    list = []
    list.append(last)
    list.append(most)
    list.append(recommended)
    return jsonify(list)
