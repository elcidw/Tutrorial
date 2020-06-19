import random
import time
import datetime
from app import app
from flask_jwt import jwt


from common.database import dbconnect
from sqlalchemy import Table

dbsession, md, DBase = dbconnect()


class Users(DBase):
    __table__ = Table('user', md, autoload=True)

    # 查询用户名，可用于注册时判断用户名是否已注册，也可用于登陆校验
    def find_by_username(self, username):
        result = dbsession.query(Users).filter_by(username=username).all()
        return result

    # 添加用户
    def do_register(self, username, password):
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        nickname = username.split('@')[0]
        avatar = str(random.randint(1, 15))
        user = Users(username=username, password=password, role='user', credit=50,
                     nickname=nickname, avatar=avatar+'.png', createtime=now, updatetime=now, is_deleted=False)
        dbsession.add(user)
        dbsession.commit()
        return user

    # 添加 JWT
    # Encode Token
    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    # Decode Token
    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))

            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
