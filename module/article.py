from common.database import dbconnect
from sqlalchemy import Table, func
from module.users import Users

dbsession, md, DBase = dbconnect()


class Article(DBase):
    __table__ = Table('article', md, autoload=True)

    @staticmethod
    def serlize(book):
        return {
            'articleid': book.articleid,
            'headline': book.headline,
            'content': book.content
        }

    def __getitem__(self, item):

        return getattr(self, item)
    # 查询所有文章

    def find_all(self):
        result = dbsession.query(Article).all()

    # 根据id查询文章, 数据格式为（Article, 'nickname')
    def find_by_id(self, articleid):
        row = dbsession.query(Article, Users.nickname).join(Users, Users.userid == Article.userid)\
            .filter(Article.hidden == 0, Article.drafted == 0, Article.checked == 1,
                    Article.articleid == articleid).first()
        return row

    # 指定分页的limit和offset的参数值，同时与用户白哦做连接查询
    def find_limit_with_users(self, start, count):
        result = dbsession.query(Article, Users.nickname).join(Users, Users.userid == Article.userid)\
            .filter(Article.hidden == 0, Article.drafted == 0, Article.checked == 1)\
            .order_by(Article.articleid.desc()).limit(count).offset(start).all()

        return result

    # 统计一下当前文章的总数量
    def get_total_count(self):
        count = dbsession.query(Article).filter(
            Article.hidden == 0, Article.drafted == 0, Article.checked == 1).count()
        return count

    # 根据文章类型获取文章
    def find_by_type(self, type, start, count):
        result = dbsession.query(Article, Users.nickname).join(Users, Users.userid == Article.userid)\
            .filter(Article.hidden == 0, Article.drafted == 0, Article.checked == 1, Article.type == type)\
            .order_by(Article.articleid.desc()).limit(count).offset(start).all()
        return result

    # 根据文章类型获取数量
    def get_count_by_type(self, type):
        count = dbsession.query(Article).filter(Article.hidden == 0, Article.drafted == 0,
                                                Article.checked == 1, Article.type == type).count()
        return count

    # 根据文章标题进行模糊搜索
    def find_by_headline(self, headline, start, count):
        result = dbsession.query(Article, Users.nickname).join(Users, Users.userid == Article.userid) \
            .filter(Article.hidden == 0, Article.drafted == 0, Article.checked == 1,
                    Article.headline.like('%'+headline+'%')) \
            .order_by(Article.articleid.desc()).limit(count).offset(start).all()
        return result

    # 统计分页总数量
    def get_count_by_headline(self, headline):
        count = dbsession.query(Article).filter(Article.hidden == 0, Article.drafted == 0,
                                                Article.checked == 1, Article.headline.like('%'+headline+'%')).count()
        return count

    # 最新文章
    def find_last_9(self):
        result = dbsession.query(Article.articleid, Article.headline)\
            .filter(Article.hidden == 0, Article.drafted == 0, Article.checked == 1)\
            .order_by(Article.articleid.desc()).limit(9).all()
        return result

    # 最多阅读
    def find_most_9(self):
        result = dbsession.query(Article.articleid, Article.headline)\
            .filter(Article.hidden == 0, Article.drafted == 0, Article.checked == 1)\
            .order_by(Article.readcount.desc()).limit(9).all()
        return result

    # 最多推荐，如果超过9篇，可以考虑order by rand()的方式
    def find_recommended_9(self):
        result = dbsession.query(Article.articleid, Article.headline)\
            .filter(Article.hidden == 0, Article.drafted == 0, Article.checked == 1, Article.recommended == 1)\
            .order_by(func.rand()).limit(9).all()
        return result

    # 一次返回三个推荐数据
    def find_last_most_recommended(self):
        last = self.find_last_9()
        most = self.find_most_9()
        recommended = self.find_recommended_9()
        print(recommended)
        return last, most, recommended

    # 每阅读一次文章，阅读次数加1
    def update_read_count(self, articleid):
        article = dbsession.query(Article).filter_by(
            articleid=articleid).first()
        article.readcount = article.readcount + 1
        dbsession.commit()

    # 根据文章编号查询文章标题
    def find_headline_by_id(self, articleid):
        row = dbsession.query(Article.headline).filter_by(
            articleid=articleid).first()
        return row.headline

    # 获取当前文章的上一篇和下一篇
    def find_prev_next_by_id(self, articleid):
        dict = {}

        # 查询比当前编号小的当中最大的一个
        row = dbsession.query(Article).filter(Article.hidden == 0, Article.drafted == 0, Article.checked == 1,
                                              Article.articleid < articleid).order_by(Article.articleid.desc()).limit(1).first()
        # 如果当前已是第一篇，上一篇也是当前文章
        if row is None:
            prev_id = articleid
        else:
            prev_id = row.articleid

        dict['prev_id'] = prev_id
        dict['prev_headline'] = self.find_headline_by_id(prev_id)

        # 查询比当前编号大的当中最小的一个
        row = dbsession.query(Article).filter(Article.hidden == 0, Article.drafted == 0, Article.checked == 1,
                                              Article.articleid > articleid).order_by(Article.articleid).limit(1).first()
        # 如果当前已是第一篇，上一篇也是当前文章
        if row is None:
            next_id = articleid
        else:
            next_id = row.articleid

        dict['next_id'] = next_id
        dict['next_headline'] = self.find_headline_by_id(next_id)

        return dict
