#encoding=utf8
import pika
import json

def init():
    credentials = pika.PlainCredentials('admin', 'admin')
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        '127.0.0.1', 5672, '/', credentials))

    cha = connection.channel()
    result = cha.queue_declare(queue='metricV1', durable=True)
    cha.exchange_declare(durable=True,
                         exchange='metricV1',
                         type='direct', )
    cha.queue_bind(exchange='metricV1',
                   queue=result.method.queue,
                   routing_key='metric', )
    # cha.basic_qos(prefetch_count=10)#消费多少条后，再批量拉
    print ' [*] Waiting for messages. To exit press CTRL+C'

    def callback(ch, method, properties, body):
        print " [x] Received %r" % (body,)
        data = json.loads(body)
        send_es(data)
        # ch.basic_ack(delivery_tag = method.delivery_tag)

    cha.basic_consume(callback,
                      queue='metricV1',
                      no_ack=True, )

    cha.start_consuming()#this is a dead


def send_es(data):
    print data

if "__main__"==__name__:
    init()
