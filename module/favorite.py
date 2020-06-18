
from flask import session

from common.database import dbconnect
from sqlalchemy import Table
import time, random

dbsession, md, DBase = dbconnect()


class Favorite(DBase):
    __table__ = Table('favorite', md, autoload=True)

    # 插入文章收藏记录
    def insert_favorite(self, articleid):
        row = dbsession.query(Favorite).filter_by(articleid=articleid, userid=session.get('userid')).first()
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        if row is not None:
            row.canceled = 0
            row.updatetime = now
        else:
            favorite = Favorite(articleid = articleid, userid = session.get('userid'), createtime = now, updatetime= now)
            dbsession.add(favorite)
        dbsession.commit()

    # 取消收藏
    def cancel_favorite(self, articleid):
        row = dbsession.query(Favorite).filter_by(articleid=articleid, userid=session.get('userid')).first()
        row.canceled = 1
        dbsession.commit()

    # 判断是否已经被收藏
    def check_favorite(self, articleid):
        row = dbsession.query(Favorite).filter_by(articleid=articleid, userid=session.get('userid')).first()
        if row is None:
            return False
        elif row.canceled == 1:
            return False
        else:
            return True