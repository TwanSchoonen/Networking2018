#!/usr/bin/env python
import pika
import time
import sys
import threading
from socketserver import ThreadedServer
from car_request import Request

serverIP = 'localhost'
serverPort = 5555

def request_from_string(message):
    print(message)
    msg = message.split(', ')
    req = Request(msg[0], msg[1], msg[2], msg[3], msg[4])
    return req


def find_car(rq):
    print("REQUEST = ")
    print("based on the message by " + rq.user_name + ", " + rq.no_passengers + " persons have to be transported from " +
          rq.location + " to " + rq.destination + ". Therefore car x is selected for the pickup")
    print(server.askLocation())

binding_key = input("Name of this center: ")
    
server = ThreadedServer(serverIP, serverPort)
thrd = threading.Thread(target = server.start_server)
thrd.setDaemon(True)
thrd.start()

if len(sys.argv) > 1:
    # example login
    credentials = pika.PlainCredentials('guest', 'guest')
    # first argument is a string
    print("seting up connection to: " + str(sys.argv[1]))
    connection = pika.BlockingConnection(pika.ConnectionParameters(str(sys.argv[1]), credentials=credentials))
else:
    print("connect to localhost, to connect to url add an argument")
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic', durable=True)

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

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