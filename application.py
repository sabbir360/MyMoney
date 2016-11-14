#!/usr/bin/env python
__author__ = 'Sabbir'
# import os

from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.options import define, options
from appcore import application


# if __name__ == '__main__':
#     port = int(os.environ.get("PORT", 8080))
#     application.run('0.0.0.0', port)


define("port", default=8088, help="run on the given port", type=int)

http_server = HTTPServer(WSGIContainer(application))
options.parse_command_line()
http_server.listen(options.port)
IOLoop.instance().start()

"""
#  from tornado.options import define, options
from gevent.wsgi import WSGIServer
from appcore import application

#  define("port", help="run on the given port", type=int)
#  import pdb; pdb.set_trace()
http_server = WSGIServer(("", 8080), application)
http_server.serve_forever()
"""
