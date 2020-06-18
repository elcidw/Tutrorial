
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# app.config.from_object('app.default_settings')
app.config.from_envvar('APP_SETTINGS')


db = SQLAlchemy(app)


if __name__ == '__main__':
    from controller.user import *
    app.register_blueprint(user)
    app.run(debug=True, host='0.0.0.0', port=5000)
