#!/usr/bin/env python
import pika
import time
import uuid
import sys
import threading
from centerserver import ThreadedServer
from centerclient import MapSocketClient
from car_request import Request

class Center:

	def __init__(self, name, messageIP, socketIP, socketPort):

		self.name = name
		
		# example login
		self.credentials = pika.PlainCredentials('guest', 'guest')

		self.connection = pika.BlockingConnection(
			pika.ConnectionParameters(host=messageIP,
									  credentials=self.credentials))
		
		self.channel = self.connection.channel()

		self.channel.exchange_declare(exchange='topic_logs',
									  exchange_type='topic',
									  durable=True)

		self.result = self.channel.queue_declare(exclusive=True)
		self.queue_name = self.result.method.queue

		
		self.channel.queue_bind(exchange='topic_logs',
		 				   queue=self.queue_name,
		 				   routing_key=self.name)

		self.channel.basic_consume(self.callback,
								   queue=self.queue_name,
								   no_ack=True)
	
	def request_from_string(self, message):
		print(message)
		msg = message.split(', ')
		req = Request(msg[0], msg[1], msg[2], msg[3], msg[4])
		return req

	def find_car(self, req):
		print("REQUEST = ")
		print("based on the message by " + req.user_name + ", " + req.no_passengers + " persons have to be transported from " +
			  req.location + " to " + req.destination + ". Therefore car x is selected for the pickup")
		# print(server.askLocation())

	def callback(self, ch, method, props, body):
		print(" [x] Received %r%r" % (method.routing_key, body))
		req = self.request_from_string(body.decode("utf-8"))
		self.find_car(req)
		time.sleep(5 + body.count(b'.'))
		print(" [x] Done")

	def start_server(self): 
		server = ThreadedServer(serverIP, serverPort)
		thrd = threading.Thread(target = server.start_server)
		thrd.setDaemon(True)
		thrd.start()

	def call(self):
		MapSocketClient('localhost', 1234).send_message(self.name)
		self.channel.start_consuming()


def main(argv):
	name = input("Name of this center: ")
	messageIP = 'localhost'
	if len(sys.argv) > 1:
		messageIP = str(argv[1])
		print("seting up connection to: " + str(argv[1]))
	else:
		print("connect to localhost, to connect to url add an argument")
	Center(name, messageIP, 'localhost', 5555).call()
  
if __name__== "__main__":
	main(sys.argv)
