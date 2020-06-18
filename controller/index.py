import math
from common.result import Result

from flask import Blueprint, render_template, abort, jsonify, session, request
from module.article import Article
from module.users import Users
from module.credit import Credit
index = Blueprint("index", __name__)
npp = 10


@index.route('/')
def home():

    article = Article()
    result = article.find_limit_with_users(0, npp)
    total = math.ceil(article.get_total_count() / npp)

    last, most, recommended = article.find_last_most_recommended()
    # 封装返回数据
    ret = Result()
    data = {}
    data['last'] = last
    data['most'] = most
    data['recommended'] = recommended
    data['total'] = total
    list = []
    for i in range(len(result)):
        data2 = {}
        data2['nickname'] = result[i][1]
        data2['articleid'] = result[i][0].articleid
        data2['headline'] = result[i][0].headline
        data2['content'] = result[i][0].content[0:80]
        list.append(data2)
    data['data'] = list
    return ret.succ(data)


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
