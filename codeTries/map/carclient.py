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
		try:
			self.sock.connect((address,port))
			self.start_client()
		except Exception as e:
			print("something's wrong with %s:%d. Exception is %s" % (address, port, e))
			self.sock.close()

	def input_handler(self):
		while True:
			data = self.sock.recv(1024)
			if not data:
				print("stoping waiting for input")
				break
			print("got from server: %s\n" % data)
			if data == str.encode("Location?"):
				self.send_location()
				
	def start_client(self):
		thrd = threading.Thread(target = self.input_handler)
		# makes sure the thread stops when main stops
		thrd.setDaemon(True)
		thrd.start()
		self.send_message("Alive!")

	def send_message(self, message):
		self.sock.send(str.encode(message))

	def send_location(self):
		send_message(str(car.pos[0]) + ', ' + str(car.pos[1]))
		
