#!/usr/bin/python
import socket
import threading

class MapSocketClient(object):
	def __init__(self, host, port):
		self.host = host
		self.port = port
		# Connect by udp
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.connect((host,port))
		
	def send_message(self, message):
		self.sock.sendto(str.encode(message), (self.host, self.port))

