'''
Init of the app
'''

from flask_sqlalchemy import SQLAlchemy
from appcore.urls import APPLICATION
from appcore.helpers.Extends import FrameExtends, ModelHelper

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
