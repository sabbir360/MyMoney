'''
User model
'''

__author__ = 'Sabbir'
from datetime import datetime

from appcore import DB


class User(DB.Model):

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    email = DB.Column(DB.String(100), unique=True, nullable=False)
    password = DB.Column(DB.String(512), nullable=False)
    create_date = DB.Column(DB.DateTime, default=datetime.now)
    update_date = DB.Column(DB.DateTime, onupdate=datetime.now)
    role = DB.Column(DB.String(50), nullable=False, default="Executor")

    def __init__(self, email=None, password=password):
        self.email = email
        self.password = password

    # Required for administrative interface
    def __unicode__(self):
        return self.username

