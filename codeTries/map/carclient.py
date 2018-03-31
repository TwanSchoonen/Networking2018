import socket
import threading

class CarClient():

	def __init__(self, address, port, car):
		self.car = car
		#networking vars
		self.address = address
		self.port = port
		# TCP
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# look if there is an center
		try:
			self.sock.connect((address,port))
			self.start_client()
		except Exception as e:
			print("something's wrong with %s:%d. Exception is %s" % (address, port, e))
			self.sock.close()

	def input_handler(self):
		try:
			while True:
				data = self.sock.recv(1024)
				if not data:
					print("stoping waiting for input")
					break
				print("got from server: %s\n" % data)
				if data == str.encode("Location?"):
					self.send_location()
		finally:
			self.sock.close()
				
	def start_client(self):
		self.send_message("Alive!")
		inputThread = threading.Thread(target = self.input_handler)
		inputThread.setDaemon(True)
		inputThread.start()

	def send_message(self, message):
		self.sock.send(message.encode("utf-8"))

	def send_location(self):
		self.send_message("Location=" +
						  str(int(self.car.pos[0] + 0.5 + self.car.distance[0])) + ', ' +
						  str(int(self.car.pos[1] + 0.5 + self.car.distance[1])))
		
