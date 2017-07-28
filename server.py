import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
from urls import urls
from tornado.options import options, define


define("port", default=10001, type=int, help="run server on the given port")



class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)

def main():
    tornado.options.parse_command_line()
    app = Application(
        urls,
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(options.port)
    http_server.start(0)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
