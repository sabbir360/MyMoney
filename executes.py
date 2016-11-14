import hashlib

from appcore import DB
from appcore.models import User

"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
"""


CONNECTION = DB.engine.connect()

DB.create_all()
CONNECTION.close()

# user = User.User('aws@me.com', hashlib.sha1('nJKa_bJADLdl%^*&D').hexdigest())
# user = User.User('aws@dhaka.com', hashlib.sha1('$faesGIudhashB*^*&D').hexdigest())
USER = User.User('sabbir', hashlib.sha1('test'.encode('utf-8')).hexdigest())
USER.role = "Super"
DB.session.add(USER)
DB.session.commit()

print(hashlib.sha1("hgsafdhfastyr62".encode('utf-8')).hexdigest())
