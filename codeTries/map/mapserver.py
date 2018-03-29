import socket
import threading

class MapServer(object):
	def __init__(self, host, port, control):
		self.host = host
		self.port = port
		self.control = control
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.bind((self.host, self.port))
		
	def start_server(self):	
		thrd = threading.Thread(target = self.server_thrd)
		thrd.setDaemon(True)
		thrd.start()

	def server_thrd(self):
		while True:
			#UDP try to get centers
			data, addr = self.sock.recvfrom(1024)
			self.control.serverEvent(data)









			

	# 	print("starting server on %s:%s" % (self.host, self.port))
	# 	self.sock.listen(5)
	# 	while True:
	# 		client, address = self.sock.accept()
	# 		# client.settimeout(60)
	# 		print("[New connection from %s:%s]:" % (address[0],address[1]))
	# 		thrd = threading.Thread(target = self.listenToClient,args = (client,address))
	# 		# makes sure the thread stops when main stops
	# 		thrd.setDaemon(True)
	# 		thrd.start()

	# def listenToClient(self, client, address):
	# 	size = 1024
	# 	while True:
	# 		try:
	# 			data = client.recv(size)
	# 			if data:
	# 				str = data.decode("utf-8")
	# 				self.control.addCenter(str)
	# 				# Set the response to echo back the recieved data 
	# 				print("got from client: %s\n" % data)
	# 				response = data
	# 				client.send(response)
	# 			else:
	# 				raise Exception('Client disconnected')
	# 		except Exception as e:
	# 			print(e)
	# 			# connection clean up
	# 			client.close()
	# 			return False
