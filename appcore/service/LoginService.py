__author__ = 'Sabbir'
from wtforms import Form, StringField, validators, PasswordField


class LoginForm(Form):
    username = StringField('Username', [validators.InputRequired()])
    password = PasswordField('Password', [validators.InputRequired()])