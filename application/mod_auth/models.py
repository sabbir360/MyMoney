'''
Auth Model
'''
__author__ = 'sabbir'
# https://flask-login.readthedocs.io/en/latest/
# https://github.com/shekhargulati/flask-login-example/blob/master/flask-login-example.py

from application import flask_login

class User(flask_login.UserMixin):
    '''
    User model
    '''
    pass
