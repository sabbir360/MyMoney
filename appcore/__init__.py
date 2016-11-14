'''
Init of the app
'''

__author__ = 'Sabbir'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from appcore.helpers.configs import *
from appcore.helpers.Extends import FrameExtends, ModelHelper

from appcore.controllers import HomeController
#  from appcore.helpers.database import db_session


APPLICATION = Flask('appcore')
APPLICATION.config['SECRET_KEY'] = SECURITY_KEY
APPLICATION.config['SQLALCHEMY_DATABASE_URI'] = DB_CONFIG
APPLICATION.config['SQLALCHEMY_ECHO'] = DEBUG_MODE
APPLICATION.debug = DEBUG_MODE
from appcore.urls import *
DB = SQLAlchemy(APPLICATION)
CONNECTION = DB.engine.connect()

APPLICATION.jinja_env.globals['url_for_other_page'] = FrameExtends.url_for_other_page


@APPLICATION.teardown_appcontext
def shutdown_session(exception=None):
    """
    Print exceptions if any inside the runtime env.
    """
    if exception:
        print(exception)
    #  db_session.remove()
    #  connection.close()
