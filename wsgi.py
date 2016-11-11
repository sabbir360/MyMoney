from gevent.wsgi import WSGIServer
from application import application as app

http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()