#!/usr/bin/env python
import pika
import time
import uuid
import sys
import threading
from centerserver import CenterServer
from centerclient import MapSocketClient
from car_request import Request

class Center:

	def __init__(self, name, messageIP, serverAddr, serverPort, amountOfCars):

		self.name = name
		self.serverAddr = serverAddr
		self.serverPort = serverPort
		self.amountOfCars = amountOfCars
		self.server = CenterServer(serverAddr, serverPort)
		self.mapClient = MapSocketClient('localhost', 1234)
		# rabbitMQ
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
		# reset the previous send locations
		self.server.locations = []
		# ask to send the new locations
		self.server.broadcast("Location?")

		# wait for all cars to respond
		while len(self.server.locations) != len(self.server.client_list):
			time.sleep(0.1)
		
		self.findClosestCar(req.clientLocation.split(','), req.destination.split(','))

	
	@staticmethod
	def getDistance(x1, y1, x2, y2):
		return abs(int(x1) - int(x2)) + abs(int(y1) - int(y2))
		

	def findClosestCar(self, clientLocation, clientDestination):
		if not self.server.locations:
			print("no available cars...")
			return
		minDistance = Center.getDistance(clientLocation[0], clientLocation[1],
										 self.server.locations[0][0], self.server.locations[0][1])
		minClient = self.server.locations[0][2]
 
		for location in self.server.locations[1:]:
			carDistance = Center.getDistance(clientLocation[0], clientLocation[1],
											 location[0], location[1]) 
			if carDistance < minDistance:
				minDistance = carDistance
				minClient = location[2]

		self.server.sendToClient("goto=" + clientLocation[0] + ',' + clientLocation[1] +
								 ", dest=" + clientDestination[0] + ',' + clientDestination[1],
								 minClient)

		
		# print("REQUEST = ")
		# print("based on the message by " + req.user_name + ", " + req.no_passengers + " persons have to be transported from " +
		# 	  req.location + " to " + req.destination + ". Therefore car x is selected for the pickup")

	def callback(self, ch, method, props, body):
		print(" [x] Received %r%r" % (method.routing_key, body))

		req = self.request_from_string(body.decode("utf-8"))
		self.mapClient.send_message("client=" + req.clientLocation + ',' + self.name)
		self.find_car(req)
		print(" [x] Done")


	def call(self):
		# start the server, talking to the cars
		self.server.start()
		# inform the map of the centers existance
		self.mapClient.send_message("center=" + self.name + ', ' +
									str(self.amountOfCars) + ', ' +
									self.serverAddr + ', ' +
									str(self.serverPort))
		# consume the message queue is blocking
		self.channel.start_consuming()


def main(argv):
	name = input("Name of this center: ")
	amountOfCars = int(input("How many cars do i have?"))
	messageIP = 'localhost'
	if len(sys.argv) > 1:
		messageIP = str(argv[1])
		print("seting up connection to: " + str(argv[1]))
	else:
		print("connect to localhost, to connect to url add an argument")
	Center(name, messageIP, 'localhost', 5555, amountOfCars).call()
  
if __name__== "__main__":
	main(sys.argv)
