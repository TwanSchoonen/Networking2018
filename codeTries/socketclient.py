import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 5555
sock.connect((host,port))
data = input("message: ")
sock.send(str.encode(data))
while True:
    print("response: ", sock.recv(1024))
