"""
Home Controller
"""

__author__ = 'sabbir'
# Import flask dependencies
from flask import Blueprint, render_template

# Import password / encryption helper tools
# from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
# from application import db

# Import module forms
# from application.mod_auth.forms import LoginForm

# Import module models (i.e. User)
# from application.mod_auth.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
MOD_HOME = Blueprint('home', __name__, url_prefix='/')

@MOD_HOME.route("/")
def index():
    """
    root function
    """
    return "Home..."

# Set the route and accepted methods
@MOD_HOME.route('/signin/', methods=['GET', 'POST'])
def signin():
    '''
    # If sign in form is submitted
    form = LoginForm(request.form)

    # Verify the sign in form
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):

            session['user_id'] = user.id

            flash('Welcome %s' % user.name)

            return redirect(url_for('auth.home'))

        flash('Wrong email or password', 'error-message')
    '''
    return render_template("auth/signin.html")
