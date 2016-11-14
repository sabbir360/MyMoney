"""
Controller base class
"""

__author__ = 'Sabbir'
from flask import flash, render_template, session, request

from appcore.helpers.configs import *
from appcore.helpers.Extends import CResponse


class Controller():
    """
    This will be the parent of all controller invoked in this app
    """
    _title = SITE_TITLE
    response_mime = 'text/html'

    def __init__(self):
        self._title = self._title+" | "+__name__

    def set_title(self, title):
        self._title = title + " | " + SITE_TITLE
        return self._title

    @staticmethod
    def set_message(message, message_type="error"):
        msg = """<div class='alert alert-""" + message_type + """ alert-dismissible' role='alert'>
                  <button type='button' class='close' data-dismiss='alert' aria-label='Close'>
                    <span aria-hidden='true'>&times;</span>
                  </button>
                  """ + message + """
                </div>"""
        return flash(msg)
        #  flash("<div class=\"alert alert-"+ message_type + "\" role=\"alert\">" + message + "</div>")
        #  return flash("<div class=\"" + message_type + "-message\">" + message + "</div>")

    def render(self, template, **context):
        """Renders a template from the template folder with the given
        context.

        :param template_name_or_list: the name of the template to be
                                      rendered, or an iterable with template names
                                      the first one existing will be rendered
        :param context: the variables that should be available in the
                        context of the template.
        """
        context['title'] = self._title
        context['app_name'] = SITE_TITLE
        return render_template(template+".html", **context)

    @staticmethod
    def get_username():
        if session.get("username"):
            return session.get("username")
        return False

    def check_authentication(self):
        return self.get_username()

    def redirect_helper(self, check_auth=True):
        """
        if get_username():
            return request.values.get("next")
        """
        if check_auth and self.check_authentication():
            return False

        return "/login?next=/" + request.url.replace(request.host_url, "")

    def response(self, response_string, status=200):

        return CResponse(response=response_string, mimetype=self.response_mime, status=status)