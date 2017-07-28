import pika
from config import rabbitmq
from tornado.web import RequestHandler


class BaseHandler(RequestHandler):

    def prepare(self):
        credentials = pika.PlainCredentials(rabbitmq.get("username"), rabbitmq.get("password"))
        self.conn = pika.BlockingConnection(pika.ConnectionParameters(
            rabbitmq.get("url"), rabbitmq.get("port"), '/', credentials))
        self.channel = self.conn.channel()
        self.channel.queue_declare(queue=rabbitmq.get("metricqueue"))
        self.channel.queue_declare(queue=rabbitmq.get("intakequeue"))


    def on_finish(self):
        self.conn.close()


















