#!/usr/bin/python
import socket
import threading
import time

class ThreadedClient(object):
    def __init__(self, host, port):
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
    
    def start_client(self):
        thrd = threading.Thread(target = self.input_handler)
        # makes sure the thread stops when main stops
        thrd.setDaemon(True)
        thrd.start()

    def send_message(self):
        data = input("message: ")
        self.sock.send(str.encode(data))
        time.sleep(0.5)

    def send_location(self):
        self.sock.send(str("1, 6").encode("utf-8"))


 
if __name__ == "__main__":
    thrdcl = ThreadedClient('localhost', 5555)
    thrdcl.start_client()
    while True:
        opt = int(input("what to do?, 1 send a message\n"))
        if opt == 1:
            thrdcl.send_message()
            
