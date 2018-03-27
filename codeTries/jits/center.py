#!/usr/bin/env python
import pika
import time
from car_request import Request


def request_from_string(message):
    print(message)
    msg = message.split(', ')
    req = Request(msg[0], msg[1], msg[2], msg[3], msg[4])
    return req


def find_car(rq):

    print("REQUEST = ")
    print("based on the message by " + rq.user_name + ", " + rq.no_passengers + " persons have to be transported from " +
          rq.location + " to " + rq.destination + ". Therefore car x is selected for the pickup")


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

binding_key = input("Name of this center: ")
channel.queue_bind(exchange='topic_logs',
                   queue=queue_name,
                   routing_key=binding_key)


def callback(ch, method, properties, body):
    print(" [x] Received %r%r" % (method.routing_key, body))
    req = request_from_string(body.decode("utf-8"))
    find_car(req)
    time.sleep(5 + body.count(b'.'))
    print(" [x] Done")


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
