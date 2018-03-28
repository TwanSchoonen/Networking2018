#!/usr/bin/python3           # This is client.py file
import socket
import sys

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
# host = socket.gethostname()     
host = 'localhost'

if len(sys.argv) != 1:
    print("supply argument")
    exit()
port = int(sys.argv[1])

# connection to hostname on the port.
s.connect((host, port))                               

# Receive no more than 1024 bytes
msg = s.recv(1024)                                     

s.close()
print (msg.decode('ascii'))
