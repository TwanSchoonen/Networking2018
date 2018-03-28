#!/usr/bin/python3           # This is server.py file
import socket                                         
import messages
import sys

class Car:
   self.available 

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = 'localhost'

if len(sys.argv) != 1:
    print("supply argument")
    exit()

port = int(sys.argv[1])

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
   # establish a connection
   clientsocket,addr = serversocket.accept()      

   print("Got a connection from %s" % str(addr))
    
   msg = 'I am available'
   # order=messages.messages.dequeueOrder();
   # msg=messages.messages.orderToCar(order);
   clientsocket.send(msg.encode('ascii'))
   clientsocket.close()
