from tornado.web import Application
from tornado import ioloop
from tornado.options import define, options, parse_command_line

from apps.urls import urls

define('port', default=8888, type=int)
parse_command_line()

app = Application(urls)

if __name__ == '__main__':
    app.listen(options.port)
    ioloop.IOLoop.current().start()
