'''
URL Builder
'''

__author__ = 'Sabbir'

from flask import Flask, session, redirect
from appcore.helpers.configs import SECURITY_KEY, DB_CONFIG, DEBUG_MODE
from appcore.controllers import HomeController
#  from appcore.helpers.database import db_session


APPLICATION = Flask('appcore')
APPLICATION.config['SECRET_KEY'] = SECURITY_KEY
APPLICATION.config['SQLALCHEMY_DATABASE_URI'] = DB_CONFIG
APPLICATION.config['SQLALCHEMY_ECHO'] = DEBUG_MODE
APPLICATION.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
APPLICATION.debug = DEBUG_MODE


#  home page
@APPLICATION.route("/")
def r_home_index():
    """
    Home route
    """
    return HomeController.HOME_CONTROLLER.index()


#  login page
@APPLICATION.route("/login", methods=['GET', 'POST'])
def r_home_login():
    """
    Login route
    """
    return HomeController.HOME_CONTROLLER.login()


@APPLICATION.route("/logout")
def logout():
    """
    Logout route
    """
    session.clear()
    return redirect("/")

"""
#  scaling
@application.route('/scaling/config')
def r_scaling_config_index():
    return scaling_config_controller.scaling_config_index()


@application.route("/scaling/config/add", methods=['POST', 'GET'])
def r_scaling_config_add():
    return scaling_config_controller.scaling_config_add()


@application.route("/scaling/config/edit", methods=['POST', 'GET'])
def scaling_config_edit():
    return scaling_config_controller.scaling_config_edit()


@application.route("/scaling/config/delete", methods=['POST'])
def scaling_config_delete():
    return scaling_config_controller.scaling_config_delete()
"""