"""
This is the file which will call by WSGI or Dev server
"""

__author__ = 'sabbir'
import flask_login
# Import flask and template operators
from flask import Flask, render_template
# Import a module /auth component using its blueprint handler variable (mod_auth)
from application.mod_auth.controllers import MOD_AUTH
from application.mod_home.controllers import MOD_HOME
# Import SQLAlchemy
# from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
APPLICATION = Flask(__name__)
APPLICATION.secret_key = 'asdhasR%rq5wre5qr51eqwe1tydwvhdf5ddsnkjeiy32672&wq76'
# login_manager = flask_login.LoginManager()
# login_manager.init_app(APPLICATION)

# Configurations
APPLICATION.config.from_object('config')


# Define the database object which is imported
# by modules and controllers
# db = SQLAlchemy(app)

# Sample HTTP error handling
@APPLICATION.errorhandler(404)
def not_found(error):
    '''
    Invoked when error occured
    '''
    print(error.__dict__)
    return render_template('404.html'), 404


# Register blueprint(s)
APPLICATION.register_blueprint(MOD_HOME)
APPLICATION.register_blueprint(MOD_AUTH)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
#  db.create_all()
