from user import User
from flask_httpauth import HTTPBasicAuth
from flask import g

auth = HTTPBasicAuth()

super = HTTPBasicAuth()

@auth.verify_password
def verify_password(username_or_token, password):
    user = User.query.filter_by(username=username_or_token).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True

@super.verify_password
def verify_password(username_or_token, password):
    return username_or_token == "root" and password == "root"
