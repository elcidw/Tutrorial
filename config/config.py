# app.config['SECRET_KEY'] = 'this is secreted'
# app.config[
#     'SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:wangyu1@localhost/flask_jwt_auth??useUnicode=true' \
#                                  '&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC '
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # True:跟踪数据库的修改，及时发送信号

import os
SECRET_KEY = 'this is secreted'

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:wangyu1@localhost/flask_jwt_auth??useUnicode=true'
SQLALCHEMY_DATABASE_URI_TEST = 'mysql+mysqlconnector://root:wangyu1@localhost/flask_jwt_auth_test??useUnicode=true'
#                                  '&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC '
# SQLALCHEMY_TRACK_MODIFICATIONS = False  # True:跟踪数据库的修改，及时发送信号

# project/server/config.py


class BaseConfig:
    """Base configuration."""
    SECRET_KEY = SECRET_KEY
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI_TEST
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = 'my_precious'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
