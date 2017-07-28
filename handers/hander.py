from handers.basehander import BaseHandler
from config import rabbitmq

class IntakeHander(BaseHandler):

    def post(self):
        body=self.request.body
        self.channel.basic_publish(exchange='',
                          routing_key=rabbitmq.get("intakequeue"),
                          body=body)
        self.finish()

class SeriesHander(BaseHandler):

    def post(self):
        body = self.request.body
        self.channel.basic_publish(exchange='',
                                   routing_key=rabbitmq.get("metricqueue"),
                                   body=body)
        self.finish()


class ServiceCheck(BaseHandler):

    def post(self):
        pass