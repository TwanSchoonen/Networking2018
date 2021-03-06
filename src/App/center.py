#!/usr/bin/env python
import pika
import time
import sys
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
		req = Request(msg[0], msg[1], msg[2], msg[3], msg[4], msg[5])
		return req

	def find_car(self, req):
		# reset the previous send locations
		self.server.locations = []
		# ask to send the new locations
		self.server.broadcast("Location?")

		# wait for all cars to respond
		while len(self.server.locations) != len(self.server.car_list):
			time.sleep(0.1)

		# find the closest car and send the client
		self.findClosestCar(req.clientLocation.split(','), req.destination_location.split(','))

	
	@staticmethod
	def getDistance(x1, y1, x2, y2):
		return abs(int(x1) - int(x2)) + abs(int(y1) - int(y2))
		

	def findClosestCar(self, clientLocation, clientDestination):

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
								 ',' + clientDestination[0] + ',' + clientDestination[1],
								 minClient)

	def callback(self, ch, method, props, body):
		# show received message
		print(" [x] Received %r%r" % (method.routing_key, body))

		# no cars available, then wait
		while not self.server.car_list:
			print("waiting for cars")
			time.sleep(1)

		# parse to get result
		req = self.request_from_string(body.decode("utf-8"))

		# send to the map that there is an client
		# so it can be drawn
		self.mapClient.send_message("client=" + self.name + ',' + req.clientLocation + ',' + req.destination_location)

		# find the car to to the work
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
	name = str(input("Name of this center: "))
	amountOfCars = int(input("How many cars do I have? "))
	center_port = int(input("Which port should be used for this center?"))
	host = 'localhost'
	messageIP = 'localhost'
	if len(sys.argv) > 1:
		messageIP = str(argv[1])
		print("seting up rabbitmq connection to: " + str(argv[1]))
	else:
		print("connect rabbitmq to localhost, to connect rabbitmq to url add it as argument")
	Center(name, messageIP, host, center_port, amountOfCars).call()
  
if __name__== "__main__":
	main(sys.argv)
