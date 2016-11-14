__author__ = 'Sabbir'
from flask import request, redirect, session, render_template
#  from appcore.helpers.database import engine
#  from appcore import connection
from appcore.helpers.Controller import Controller


class HomeController(Controller):

    def index(self):
        """
        Home page
        """
        #  results = engine.connect().execute("SELECT * FROM tbl_golf_course LIMIT 5")
        #  connection = db.engine.connect()
        #  print results
        self.set_title("Home")
        return self.render("home/index")

    def login(self):
        """
        Login Page
        """
        self.set_title("Login")

        import hashlib
        from appcore.models.User import User
        from appcore.service.LoginService import LoginForm
        form = LoginForm(request.form)
        back_url = request.values.get("next")
        if request.method == "POST" and form.validate():
            model = User().query.filter_by(email=form.username.data).first()

            if model and model.password == hashlib.sha1(form.password.data).hexdigest():
                session['username'] = model.email
                session['role'] = model.role
                return redirect(back_url)
            self.set_message("Invalid username or password!")

        return self.render("home/login", form=form)

    def simple_read(self):
        """
        Simple read example
        """
        from appcore.models.InstanceCommand import InstanceCommand
        data = InstanceCommand().query.all()
        for row in data:
            print(row.name)
            print(row.command)
        return self.render("home/index")

HOME_CONTROLLER = HomeController()
