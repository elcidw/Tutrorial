from flask import Blueprint, abort, render_template, request
from module.article import Article
from module.credit import Credit
from module.users import Users
from module.favorite import Favorite

article = Blueprint('article', __name__)


@article.route('/article/<int:articleid>')
def read(articleid):
    try:
        # 数据格式：(Article, 'nickname')
        result = Article().find_by_id(articleid)
        if result is None:
            abort(404)
    except:
        abort(500)

    dict = {}
    for k, v in result[0].__dict__.items():
        if not k.startswith('_sa_instance_state'):
            dict[k] =  v
        dict['nickname'] = result.nickname

    # 需要积分阅读时，显示一半文章, 如果已经消费，则显示全部
    payed = Credit().check_payed_article(articleid)
    position=0
    if not payed:
        content = dict['content']
        temp = content[0:int(len(content)/3)]
        position = temp.rindex('</p>')+4
        dict['content'] = temp[0:position]

    Article().update_read_count(articleid)

    is_favorited = Favorite().check_favorite(articleid)

    # 获取当前文章的上一篇和下一篇

    prev_next = Article().find_prev_next_by_id(articleid)

    return render_template('article-user.html', article=dict, position = position, payed = payed, \
                           is_favorited=is_favorited, prev_next=prev_next)

@article.route('/readall', methods=['post'])
def read_all():
    position = int(request.form.get('position'))
    articleid = request.form.get('articleid')
    article = Article()
    result = article.find_by_id(articleid)
    content = result[0].content[position:]

    # 如果已经消耗积分，则不再扣除
    payed = Credit().check_payed_article(articleid)
    if not payed:
        # 处理积分
        Credit().insert_detail(type="阅读文章",target=articleid, credit=-1*result[0].credit)
        Users().update_credit( credit=-1*result[0].credit)

    return content
