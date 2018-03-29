import socket
import threading

class socketcar(object):
	self.dest
	def __init__(self, pos, host, port):

		self.isAvailable = True
		self.pos = pos
		self.clientdest=clientdest
		#networking vars
		self.host = host
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((host,port))
	
	def input_handler(self):
		while True:
			data = self.sock.recv(1024)
			if not data:
				print("stoping waiting for input")
				break
			print("got from server: %s\n" % data)
			if data == str.encode("Location?"):
				self.send_location()
				
	def send_location(self):
		pass
				
	def changeLocation(self):
		if(self.pos!=self.dest):
			x=self.pos[0]
			y=self.pos[1]
			x1=self.dest[0]
			y1=self.dest[1]
			if x<x1:
				x+=1
			elif x>x1:
				x-=1
			elif y<y1:
				y+=1
			elif y>y1:
				y-=1
				self.pos=(x,y)
		return(self.pos)
	
	def setNewDest(self,isAvailable,clientIndex,dest,clientdest):
		self.isAvailable = isAvailable
		self.dest = dest
		self.clientdest=clientdest
		self.clientIndex=clientIndex
