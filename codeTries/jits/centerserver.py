#!/usr/bin/python
import socket
import threading

BUFFSIZE = 1024

class CenterServer(object):
	def __init__(self, host, port):
		self.host = host
		self.port = port
		# list with clients and a used lock
		self.car_list = set()
		self.client_lock = threading.Lock()
		self.locations = []
		self.availableCars = []

	def start(self):
		listener = threading.Thread(target = self.listener)
		listener.setDaemon(True)
		listener.start()
		
	def listener(self):
		print("starting server on %s:%s" % (self.host, self.port))
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			sock.bind((self.host, self.port))
		except Exception as e:
			print("Problem making new server on this port. Exception: " + str(e))
		sock.listen(5)

		while True:
			client, address = sock.accept()
			print("[New connection from %s:%s]:" % (address[0],address[1]))

			with self.client_lock:
				self.car_list.add(client)

			clientThread = threading.Thread(target=self.listenToClient,
											args=(client,))
			clientThread.setDaemon(True)
			clientThread.start()


	def broadcast(self, message):
		for c in self.car_list:
			c.send(message.encode("utf-8"))

	def sendToClient(self, message, client):
		if message.startswith("goto="):
			self.car_list.remove(client)
			client.send(message.encode("utf-8"))

	def listenToClient(self, client):
		try:
			while True:
				data = client.recv(BUFFSIZE)
				if not data:
					break
				message = data.decode("utf-8")
				if (message.startswith("Location=")):
					loc = message.split("=")[1]
					coord = loc.split(", ")
					self.locations.append((int(coord[0]), int(coord[1]), client))
					print("got location:" + message)
				elif (message == "available"):
					print("car is available")
					self.car_list.add(client)
				else:
					print("got from client: %s\n" % data)

		except Exception as e:
			print(e)
		finally:
			# connection clean up
			with self.client_lock:
				print("remove client")
				self.car_list.remove(client)
				client.close()
				return False
