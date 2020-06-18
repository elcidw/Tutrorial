from flask import Blueprint, make_response, session, request, redirect, url_for
from common.utility import ImageCode, gen_email_code, send_email
from module.users import Users
from module.credit import Credit
from module.favorite import Favorite
favorite = Blueprint('favorite', __name__)

@favorite.route('/favorite', methods=['POST'])
def add_favorite():
    articleid = request.form.get('articleid')
    if session.get('islogin') is None:
        return 'not-login'
    else:
        try:
            Favorite().insert_favorite(articleid)
            return 'favorite-pass'
        except:
            return 'favorite-fail'

@favorite.route('/favorite/<int:articleid>',methods=['delete'])
def cancel_favorite(articleid):
    try:
        Favorite().cancel_favorite(articleid)
        return 'cancel-pass'
    except:
        return 'cancel-fail'