'''
URL Builder
'''

__author__ = 'Sabbir'
from appcore import APPLICATION
#  from flask import request


from appcore.controllers.HomeController import HOME_CONTROLLER
from flask import session, redirect


#  home page
@APPLICATION.route("/")
def r_home_index():
    """
    Home route
    """
    return HOME_CONTROLLER.index()


#  login page
@APPLICATION.route("/login", methods=['GET', 'POST'])
def r_home_login():
    """
    Login route
    """
    return HOME_CONTROLLER.login()


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